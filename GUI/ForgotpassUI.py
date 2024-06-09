from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designforgotpassUI import Ui_forgotPassword
from GUI.changepassUI import ChangePass
from user import User
class ForgotPass(QDialog, Ui_forgotPassword):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.User = User()
        self.forgotPassCancelBtn.clicked.connect(self.forgotcancelHandler)
        self.forgotPassSubmitBtn.clicked.connect(self.forgotpassHandler)

#adminIDInput
    def forgotcancelHandler(self):
        self.close()


    def forgotpassHandler(self):
        adminID = self.adminIDInput.text()
        username = self.usernameInput.text()
        
        if (adminID and username) == "":
                print(adminID, username, )
                noInput = QMessageBox()
                noInput.setWindowTitle("Error")
                noInput.setIcon(QMessageBox.Icon.Warning)
                noInput.setText("Please input Admin ID or Username")
                noInput.exec()

        elif self.User.cp_validate_user(adminID, username):
            #validation here 
            self.hide()
            changepass = ChangePass(adminID)
            changepass.exec()
            
            self.close()
        else:
                noInput = QMessageBox()
                noInput.setWindowTitle("Error")
                noInput.setIcon(QMessageBox.Icon.Warning)
                noInput.setText("Invalid Username or Admin ID")
                noInput.exec()
           


