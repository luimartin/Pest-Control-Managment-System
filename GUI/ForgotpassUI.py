from PyQt6.QtWidgets import QApplication, QDialog
from designforgotpassUI import Ui_forgotPassword

class ForgotPass(QDialog, Ui_forgotPassword):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.forgotPassCancelBtn.clicked.connect(self.forgotcancelHandler)

    def forgotcancelHandler(self):
        self.close()


