import sys
import serial
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLineEdit, QLabel, QHBoxLayout

class GSMApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.ser = None

    def initUI(self):
        self.setWindowTitle('GSM Module Controller')

        # Create input fields for phone number and message
        self.phoneNumberLabel = QLabel('Phone Number:', self)
        self.phoneNumberInput = QLineEdit(self)

        self.messageLabel = QLabel('Message:', self)
        self.messageInput = QLineEdit(self)

        # Create a button to send the message
        self.sendButton = QPushButton('Send Message', self)
        self.sendButton.clicked.connect(self.send_message)

        # Create a text area to display responses
        self.responseText = QTextEdit(self)
        self.responseText.setReadOnly(True)

        # Set up the layout
        formLayout = QVBoxLayout()
        formLayout.addWidget(self.phoneNumberLabel)
        formLayout.addWidget(self.phoneNumberInput)
        formLayout.addWidget(self.messageLabel)
        formLayout.addWidget(self.messageInput)
        formLayout.addWidget(self.sendButton)

        layout = QVBoxLayout()
        layout.addLayout(formLayout)
        layout.addWidget(self.responseText)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def connect_serial(self):
        # Replace 'COM5' with the appropriate port for your system
        self.ser = serial.Serial('COM5', 9600, timeout=1)
        time.sleep(2)  # Wait for the serial connection to initialize

    def send_at_command(self, command, wait_time=1):
        self.ser.write((command + '\r\n').encode())
        time.sleep(wait_time)
        response = self.ser.read(self.ser.inWaiting()).decode()
        return response

    def send_message(self):
        if not self.ser:
            self.connect_serial()

        phone_number = self.phoneNumberInput.text()
        message = self.messageInput.text()

        # Set SMS mode to text
        response = self.send_at_command('AT+CMGF=1')
        self.responseText.append(f"Command: AT+CMGF=1\nResponse: {response}\n")

        # Send SMS
        response = self.send_at_command(f'AT+CMGS="{phone_number}"')
        self.responseText.append(f"Command: AT+CMGS=\"{phone_number}\"\nResponse: {response}\n")

        # Send the message content
        self.ser.write((message + '\x1A').encode())  # '\x1A' is the ASCII code for Ctrl+Z, which signals the end of the message
        time.sleep(3)  # Wait for the message to be sent
        response = self.ser.read(self.ser.inWaiting()).decode()
        self.responseText.append(f"Message: {message}\nResponse: {response}\n")

    def closeEvent(self, event):
        if self.ser:
            self.ser.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GSMApp()
    window.show()
    sys.exit(app.exec())