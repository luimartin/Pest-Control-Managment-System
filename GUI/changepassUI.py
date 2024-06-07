from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designchangepass import Ui_changePassword

class ChangePass(QDialog, Ui_changePassword):

    def __init__(self,adminID):
        super().__init__()
        self.setupUi(self)

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
        else:
            #change pass here
            print("may input")
            