from PyQt6.QtWidgets import QDialog,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton
from PyQt6 import QtGui, QtCore
from GUI.designeditclientUI import Ui_Dialog
from clientinfo import ClientInfo
from user import User
class editClients(QDialog,Ui_Dialog):
    def __init__(self, client_id, admin):
        self.c =ClientInfo()
        super().__init__()
        self.id = client_id
        self.setupUi(self)
        self.u = User()
        self.admin = admin
        regex = QtCore.QRegularExpression(r"^0\d{0,10}$")
        validator = QtGui.QRegularExpressionValidator(regex, self)
        self.contactnoInput.setValidator(validator)
        self.emailBtn.clicked.connect(self.editname)
        self.cancelBtn.clicked.connect(lambda: self.close())
        placeholder = self.c.get_data(self.id, ("name, phone_num, address, email"))
        self.nameInput.setText(placeholder[0][0])
        self.contactnoInput.setText(placeholder[0][1])
        self.locationInput.setText(placeholder[0][2])
        self.emailInput.setText(placeholder[0][3])
    
    def notif(self, name):
        noInput = QMessageBox()
        noInput.setIcon(QMessageBox.Icon.Information)
        noInput.setText("{} Changed".format(name))
        noInput.exec()

    def editname(self):
        name = self.nameInput.text()
        contact=self.contactnoInput.text()
        email=self.emailInput.text()
        loc=self.locationInput.text()
        self.c.edit_personal_info(self.id, 'name', name)
        self.c.edit_personal_info(self.id, 'phone_num', contact)
        self.c.edit_personal_info(self.id, 'address', loc)
        self.c.edit_personal_info(self.id, 'email', email)
        self.u.add_backlogs(self.admin, "Edited Client")
        self.notif("Client Information")
        self.close()
        
