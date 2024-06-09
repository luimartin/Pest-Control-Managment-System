from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designchangepass import Ui_changePassword
from user import User
class ChangePass(QDialog, Ui_changePassword):

    def __init__(self,adminID):
        super().__init__()
        self.setupUi(self)
        self.User = User()
        self.adminID = adminID
        self.changePassSubmitBtn_2.clicked.connect(self.changepassHandler)
    
    def changepassHandler(self):
        newpass = self.newpassword.text()
        confirmpass = self.confirmpassword.text()
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
