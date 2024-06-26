import sys
import matplotlib
matplotlib.use('QtAgg')

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sales import Sales

class SaleTrendDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Monthly Total Sale')
        self.setGeometry(100, 100, 800, 600)
        self.sale = Sales()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.plot_widget = SaleTrendWidget()
        layout.addWidget(self.plot_widget)
        #self.show()

class SaleTrendWidget(FigureCanvasQTAgg):
    def __init__(self):
        self.sale = Sales()
        data = self.sale.monthly_total_sale()
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        super().__init__(self.fig)

        # Convert the month names to month numbers
        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        dates = []
        for row in data:
            year = row[0]
            month_name = row[1]
            month_num = month_names.index(month_name) + 1
            date_str = f"{year}-{month_num:02d}"
            dates.append(date_str)
        total = [row[2] for row in data]

        self.ax.plot(dates, total, marker='o', linestyle='-')
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Total Sale')
        self.ax.set_title('Monthly Total Sale')
        self.ax.tick_params(axis='x', rotation=45)
        self.ax.grid(True)

        window_size = 3
        moving_avg = []
        for i in range(len(total) - window_size + 1):
            avg = sum(total[i:i+window_size]) / window_size
            moving_avg.append(avg)

        last_date = datetime.strptime(dates[-1], '%Y-%m')
        next_dates = [last_date + relativedelta(months=i) for i in range(1, 4)]

        last_value = total[-1]
        prediction = [last_value] * 3

        self.ax.plot(dates[:-window_size+1], moving_avg, color='red', linestyle='--', label='Moving Average')
        self.ax.plot([date.strftime('%Y-%m') for date in next_dates], prediction, color='green', linestyle='--', label='Predicted Total Sale')
        self.ax.legend()

        self.fig.tight_layout()