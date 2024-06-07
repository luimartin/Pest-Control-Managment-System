import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel

class FirstDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Dialog")
        
        # Layout and widgets
        layout = QVBoxLayout()
        self.input_field = QLineEdit(self)
        self.pass_value_button = QPushButton("Pass Value", self)
        
        layout.addWidget(self.input_field)
        layout.addWidget(self.pass_value_button)
        self.setLayout(layout)
        
        # Connect the button to the method to open the second dialog
        self.pass_value_button.clicked.connect(self.open_second_dialog)
    
    def open_second_dialog(self):
        value_to_pass = self.input_field.text()
        second_dialog = SecondDialog(value_to_pass)
        second_dialog.exec()

class SecondDialog(QDialog):
    def __init__(self, value):
        super().__init__()
        self.setWindowTitle("Second Dialog")
        
        # Layout and widgets
        layout = QVBoxLayout()
        self.label = QLabel(f"Received value: {value}", self)
        
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    first_dialog = FirstDialog()
    first_dialog.show()
    
    sys.exit(app.exec())
