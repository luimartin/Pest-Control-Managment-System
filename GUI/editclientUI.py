from PyQt6.QtWidgets import QApplication, QDialog,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton
from GUI.designeditclientUI import EditClient
from clientinfo import ClientInfo
class editClients(QDialog,EditClient):
    def __init__(self, client_id):
        self.c =ClientInfo()
        super().__init__()
        self.id = client_id
        self.setupUi(self)
        self.nameBtn.clicked.connect(lambda:self.editname(self.nameInput, 1))
        self.contactnoBtn.clicked.connect(lambda:self.editname(self.contactnoInput, 2))
        self.locationBtn.clicked.connect(lambda:self.editname(self.locationInput, 3))
        self.emailBtn.clicked.connect(lambda:self.editname(self.emailInput, 4))
        self.cancelBtn.clicked.connect(self.cancel)

    def notif(self, name):
        noInput = QMessageBox()
        noInput.setIcon(QMessageBox.Icon.Information)
        noInput.setText("{} Changed".format(name))
        noInput.exec()
    def editname(self, input, categ):
        lagay = input.text()
        if categ == 1:
            self.c.edit_personal_info(self.id, 'name', lagay)
            self.notif("Name")
        elif categ == 2:
            self.c.edit_personal_info(self.id, 'phone_num', lagay)
            self.notif("Contact No.")
        elif categ == 3:
            self.c.edit_personal_info(self.id, 'address', lagay)
            self.notif("Address")
        else:
            self.c.edit_personal_info(self.id, 'email', lagay)
            self.notif("Email")
        input.clear()
    def cancel(self):
        self.close()
        
