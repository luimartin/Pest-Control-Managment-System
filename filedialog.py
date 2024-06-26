import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QFileDialog, 
    QGridLayout,
    QPushButton, 
    QLabel,
    QListWidget
)
from pathlib import Path


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100, 100, 300, 150)

        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browser_btn = QPushButton('Browse')
        file_browser_btn.clicked.connect(self.open_file_dialog)

        self.file_list = QListWidget(self)

        layout.addWidget(QLabel('Files:'), 0, 0)
        layout.addWidget(self.file_list, 1, 0)
        layout.addWidget(file_browser_btn, 2 ,0)

        self.show()

    def open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'C:\Users\deini\OneDrive\Desktop\backup')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("SQl (*.sql)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                # Extract filenames without directory path
                filenames = [Path(filename).name for filename in filenames]
                print(filenames)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
