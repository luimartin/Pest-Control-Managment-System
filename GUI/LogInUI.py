from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI.designLoginUI import Ui_login
from PyQt6 import QtGui, QtWidgets
from GUI.ForgotpassUI import ForgotPass
from user import User
from MainmenuUI import MainMenu
class Window(QMainWindow, Ui_login):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.User = User()
        self.setWindowTitle("HomeFix LogIn")
        self.submitBtn.clicked.connect(self.loginHandler)
        self.forgotpassworBtn.clicked.connect(self.forgotPassHandler)
        self.adminIDInput.setValidator(QtGui.QIntValidator())
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    
    def loginHandler(self):
        adminID = self.adminIDInput.text()
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if (adminID and username and password) == "":
            print("wala laman")
            self.notif(QMessageBox.Icon.Warning, "Fields cannot be null")
            
        elif self.User.validate_user(adminID, password):
            print("mayinput")
            self.User.add_backlogs(adminID, "User Login")
            self.hide()
            main = MainMenu(adminID, self)
            self.adminIDInput.clear()
            self.usernameInput.clear()
            self.passwordInput.clear()
            main.show()
            #self.show()
            ## mainmenu here 

            
        else: 
            print("mali input")
            self.notif(QMessageBox.Icon.Warning, "Wrong Credentials")

    def forgotPassHandler(self):
        forgotdialog = ForgotPass()
        forgotdialog.exec()
        
    def notif(self, icon, msg):
        noInput = QMessageBox()
        noInput.setWindowTitle("HomeFix")
        noInput.setIcon(icon)
        noInput.setText(msg)
        noInput.exec()
        




