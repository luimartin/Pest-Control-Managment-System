from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from designchangepass import Ui_changePassword

class ChangePass(QDialog, Ui_changePassword):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
