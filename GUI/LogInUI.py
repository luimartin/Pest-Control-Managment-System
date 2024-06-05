from PyQt6.QtWidgets import QApplication, QMainWindow
from designLoginUI import Ui_login
from ForgotpassUI import ForgotPass
class Window(QMainWindow, Ui_login):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submitBtn.clicked.connect(self.loginHandler)
        self.forgotpassworBtn.clicked.connect(self.forgotPassHandler)
    
    def loginHandler(self):
        print("yey")
        adminID = self.adminIDInput.text()
        username = self.usernameInput.text()
        password = self.passwordInput.text()

        print(adminID, username, password)

        #put validation shit here......

        

    def forgotPassHandler(self):
        forgotdialog = ForgotPass()
        forgotdialog.exec()
        


app = QApplication([])
window = Window()

window.show()
app.exec()

