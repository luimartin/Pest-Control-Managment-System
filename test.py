import sys
from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem,
    QPushButton, QLabel, QDialog, QTextEdit, QSizePolicy
)
from PyQt6.QtCore import QDate, Qt, QLocale
from PyQt6.QtGui import QFont, QTextCursor
from schedule import Schedule

class ScheduleDialog(QDialog):
    def __init__(self, client_name, schedule, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Schedule for {client_name}")

        layout = QVBoxLayout()

        # Create a QLabel for the time and center it
        time_label = QLabel("Service Time")
        time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(16)
        time_label.setFont(font)

        self.schedule_text = QTextEdit()
        schedule_text = '\n'.join(schedule)
        self.schedule_text.setText(schedule_text)
        self.schedule_text.setReadOnly(True)

        # Set font size to 16px
        self.schedule_text.setStyleSheet("font-size: 16px; text-align: center;")

        # Align text to center
        cursor = self.schedule_text.textCursor()
        cursor.select(QTextCursor.SelectionType.Document)
        cursor.mergeBlockFormat(self.center_alignment())
        cursor.clearSelection()
        self.schedule_text.setTextCursor(cursor)

        layout.addWidget(time_label)
        layout.addWidget(self.schedule_text)
        self.setLayout(layout)

    def center_alignment(self):
        format = QTextCursor().blockFormat()
        format.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return format

class CalendarScheduler(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar Scheduler")
        self.setGeometry(100, 100, 1209, 768)

        self.central_widget = QWidget()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        ####### THIS IS WHERE THE INTIALIZATION OF TIMETABLE BEGINS #######
        s = Schedule()
        self.scheduled_events = {}
        self.scheduled_events = s.timetable(self.scheduled_events)

        self.add_month_year_label()
        self.create_calendar_table()
        self.populate_calendar()

    def add_month_year_label(self):
        current_date = QDate().currentDate()
        month_year_label = QLabel(current_date.toString("MMMM yyyy"), self)
        month_year_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = month_year_label.font()
        font.setPointSize(16)
        month_year_label.setFont(font)
        self.layout.addWidget(month_year_label)

    def create_calendar_table(self):
        current_date = QDate().currentDate()
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

        # Set background color for the headers
        self.calendar_table.setStyleSheet("QHeaderView::section { background-color: #2D7401; color: white }")

        # Set font size for headers
        header_font = self.calendar_table.horizontalHeader().font()
        header_font.setPointSize(14)  # Adjust the font size here
        self.calendar_table.horizontalHeader().setFont(header_font)

        self.layout.addWidget(self.calendar_table)

    def populate_calendar(self):
        current_date = QDate().currentDate()
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
                    button.setStyleSheet("background-color: #E3C55C;")  # Set button background color
                    button.clicked.connect(lambda checked, n=client_name, s=schedule: self.show_schedule(n, s))
                    cell_layout.addWidget(button)

            cell_widget.setLayout(cell_layout)

            # Set background color for the cell
            cell_widget.setStyleSheet("background-color: #F4FCF5;")

            self.calendar_table.setCellWidget(row, column, cell_widget)

    def calculate_position(self, date):
        first_day = QDate(date.year(), date.month(), 1).dayOfWeek()
        row = (date.day() + first_day - 2) // 7
        column = (date.dayOfWeek() + 6) % 7  # Adjust for Sunday being the first day
        return row, column

    def show_schedule(self, client_name, schedule):
        dialog = ScheduleDialog(client_name, schedule, self)
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CalendarScheduler()
    main_window.show()
    sys.exit(app.exec())
