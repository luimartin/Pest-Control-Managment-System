from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designaddclientUI import Ui_addClients
from clientinfo import ClientInfo
from user import User
class addClient(QDialog, Ui_addClients):
    def __init__(self, admin):
        super().__init__()
        self.setupUi(self)
        self.c = ClientInfo()
        self.u = User()
        self.admin = admin
        regex = QtCore.QRegularExpression(r"^0\d{0,10}$")
        validator = QtGui.QRegularExpressionValidator(regex, self)
        self.phonenumInput.setValidator(validator)
        self.addclientBtn.clicked.connect(self.addclient)
        self.cancelBtn.clicked.connect(lambda: self.close())

    def addclient(self):
        name = self.nameInput.text()
        email = self.emailInput.text()
        phoneno = self.phonenumInput.text()
        address = self.addressInput.text()
        
        if (name, email, phoneno, address) == "":
            self.notif(QMessageBox.Icon.Warning, "Fields should cannot be null")
  

        else:
            self.c.add_client_info(name, email, phoneno, address)
            self.notif(QMessageBox.Icon.Information, "Client Information")
            self.u.add_backlogs(self.admin, "Added Client")
            self.close()
    
    def notif(self, icon, msg):
        noInput = QMessageBox()
        noInput.setWindowTitle("Clients")
        noInput.setIcon(icon)
        noInput.setText(msg)
        noInput.exec()








