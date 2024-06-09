from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designaddclientUI import Ui_addClients
from clientinfo import ClientInfo
class addClient(QDialog, Ui_addClients):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.c = ClientInfo()

        self.addclientBtn.clicked.connect(self.addclient)
        self.cancelBtn.clicked.connect(self.cancel)

    def addclient(self):
        name = self.nameInput.text()
        email = self.emailInput.text()
        phoneno = self.phonenumInput.text()
        address = self.addressInput.text()
        self.c.add_client_info(name, email, phoneno, address)

        noInput = QMessageBox()
        noInput.setWindowTitle("Clients")
        noInput.setIcon(QMessageBox.Icon.Information)
        noInput.setText("Client Added")
        noInput.exec()
        self.close()

    def cancel(self):
        self.close()




