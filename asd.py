from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()
window.setLayout(layout)

table = QTableWidget(3, 3)  # 3 rows, 3 columns

# Set the headers
table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

# Populate the table with data and set the text alignment
for row in range(3):
    for col in range(3):
        item = QTableWidgetItem(f"Item {row},{col}")
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        table.setItem(row, col, item)

layout.addWidget(table)
window.show()
sys.exit(app.exec())