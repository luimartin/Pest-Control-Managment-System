from PyQt6.QtWidgets import QDialog,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton
from GUI.designeditclientUI import Ui_Dialog
from clientinfo import ClientInfo
class editClients(QDialog,Ui_Dialog):
    def __init__(self, client_id):
        self.c =ClientInfo()
        super().__init__()
        self.id = client_id
        self.setupUi(self)
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
        self.notif("Client Information")
        
