from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI.designLoginUI import Ui_login
from GUI.ForgotpassUI import ForgotPass
from user import User

class Window(QMainWindow, Ui_login):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.User = User()
        self.submitBtn.clicked.connect(self.loginHandler)
        self.forgotpassworBtn.clicked.connect(self.forgotPassHandler)
    
    def loginHandler(self):
        adminID = self.adminIDInput.text()
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if (adminID and username and password) == "":
            print("wala laman")
            noInput = QMessageBox()
            noInput.setWindowTitle("Error")
            noInput.setIcon(QMessageBox.Icon.Warning)
            noInput.setText("Please input Admin ID or Username or Password")
            noInput.exec()

        elif self.User.validate_user(adminID, password):
            print("mayinput")
            #validation shit here......
        else: 
            print("mali input")

    def forgotPassHandler(self):
        forgotdialog = ForgotPass()
        forgotdialog.exec()
        
        




