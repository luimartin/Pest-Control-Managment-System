import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
import matplotlib.pyplot as plt
import random
from sales import Sales
class SaleTrendDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib with PyQt6")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.s = Sales()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Generate mock data (replace with your actual data loading logic)
        data = self.s.monthly_total_sale()

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

        plt.rcParams['toolbar'] = 'None'
        plt.figure(figsize=(10, 6))
        plt.plot(dates, total, marker='o', linestyle='-')
        plt.xlabel('Date')
        plt.ylabel('Total Sale')
        plt.title('Monthly Total Sale')
        plt.xticks(rotation=45)
        plt.grid(True)

        window_size = 3
        moving_avg = []
        for i in range(len(total) - window_size + 1):
            avg = sum(total[i:i+window_size]) / window_size
            moving_avg.append(avg)

        plt.plot(dates[:-window_size+1], moving_avg, color='red', linestyle='--', label='Moving Average')
        plt.legend()

        plt.tight_layout()

        # Create matplotlib widget
        self.canvas = plt.gcf()
        layout.addWidget(self.canvas.canvas)


