from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit
from GUI.designchangepass import Ui_changePassword
from user import User
class ChangePass(QDialog, Ui_changePassword):

    def __init__(self,adminID):
        super().__init__()
        self.setupUi(self)
        self.User = User()
        self.adminID = adminID
        self.User = User()
        self.adminID = adminID
        self.changePassSubmitBtn_2.clicked.connect(self.changepassHandler)
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
    
    def changepassHandler(self):
        newpass = self.lineEdit.text()
        confirmpass = self.lineEdit_2.text()
        if (newpass and confirmpass) == "":
            noInput = QMessageBox()
            noInput.setWindowTitle("Error")
            noInput.setIcon(QMessageBox.Icon.Warning)
            noInput.setText("Please input password")
            noInput.exec()
        elif self.User.new_pass(self.adminID,newpass,confirmpass):
            noInput = QMessageBox()
            noInput.setWindowTitle("Password")
            noInput.setIcon(QMessageBox.Icon.Information)
            noInput.setText("Password Updated")
            noInput.exec()
            self.close()
        else:
            noInput = QMessageBox()
            noInput.setWindowTitle("Error")
            noInput.setIcon(QMessageBox.Icon.Warning)
            noInput.setText("Password Mismatch")
            noInput.exec()
