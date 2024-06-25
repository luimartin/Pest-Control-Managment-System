import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem,
    QPushButton, QLabel, QDialog, QTextEdit, QSizePolicy
)
from PyQt6.QtCore import QDate, Qt, QLocale
from schedule import Schedule

class ScheduleDialog(QDialog):
    def __init__(self, client_name, schedule, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Schedule for {client_name}")

        layout = QVBoxLayout()
        self.schedule_text = QTextEdit()

        schedule_text = '\n'.join(schedule)
        self.schedule_text.setText(schedule_text)
        self.schedule_text.setReadOnly(True)

        layout.addWidget(self.schedule_text)
        self.setLayout(layout)

class CalendarScheduler(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar Scheduler")
        self.setGeometry(100, 100, 1209, 768)

        self.central_widget = QWidget()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.central_widget)
        #self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        ####### THIS IS WHERE THE INTIALIZATION OF TIMETABLE BEGINS #######
        s = Schedule()
        self.scheduled_events = {}
        self.scheduled_events = s.timetable(self.scheduled_events)

        self.create_calendar_table()
        self.populate_calendar()

    def create_calendar_table(self):
        current_date = QDate(2024, 7, 1)
        first_day_of_month = QDate(current_date.year(), current_date.month(), 1)
        days_in_month = first_day_of_month.daysInMonth()
        start_day_of_week = first_day_of_month.dayOfWeek()

        # Calculate number of weeks needed
        weeks_in_month = (days_in_month + start_day_of_week - 1 + 6) // 7

        # Set the table size dynamically based on weeks
        table_width = 1209
        table_height = 768
        self.calendar_table = QTableWidget(weeks_in_month, 7, self)
        self.calendar_table.setFixedSize(table_width, table_height)

        # Set horizontal headers dynamically based on localized day names
        day_names = [QLocale().standaloneDayName(i, QLocale.FormatType.LongFormat) for i in range(1, 8)]
        self.calendar_table.setHorizontalHeaderLabels(day_names)
        self.calendar_table.verticalHeader().setVisible(False)

        # Adjust the column and row sizes
        for i in range(7):
            self.calendar_table.setColumnWidth(i, table_width // 7)
        for i in range(weeks_in_month):
            self.calendar_table.setRowHeight(i, table_height // weeks_in_month)

        self.layout.addWidget(self.calendar_table)

    def populate_calendar(self):
        current_date = QDate(2024, 7, 1) # to debug use QDate(2024, 7, 1)
        first_day_of_month = QDate(current_date.year(), current_date.month(), 1)

        for day in range(1, first_day_of_month.daysInMonth() + 1):
            date = QDate(current_date.year(), current_date.month(), day)
            row, column = self.calculate_position(date)

            cell_widget = QWidget()
            cell_layout = QVBoxLayout()
            cell_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

            day_label = QLabel(f"{day}")
            cell_layout.addWidget(day_label)

            date_str = date.toString("yyyy-MM-dd")
            if date_str in self.scheduled_events:
                for client_name, schedule in self.scheduled_events[date_str].items():
                    button = QPushButton(client_name)
                    button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
                    button.clicked.connect(lambda checked, n=client_name, s=schedule: self.show_schedule(n, s))
                    cell_layout.addWidget(button)

            cell_widget.setLayout(cell_layout)
            self.calendar_table.setCellWidget(row, column, cell_widget)

    def calculate_position(self, date):
        first_day = QDate(date.year(), date.month(), 1).dayOfWeek()
        row = (date.day() + first_day - 2) // 7
        column = (date.dayOfWeek() + 6) % 7  # Adjust for Sunday being the first day
        return row, column

    def show_schedule(self, client_name, schedule):
        dialog = ScheduleDialog(client_name, schedule, self)
        dialog.exec()

