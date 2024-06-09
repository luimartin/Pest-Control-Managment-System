from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox,QTableWidget,QTableWidgetItem,QHeaderView
from GUI.designMainMenu import Ui_MainWindow
from clientinfo import ClientInfo
from GUI.addclientUI import addClient
class MainMenu(QMainWindow, Ui_MainWindow):
    def __init__(self, AdminID):
        super().__init__()
        self.setupUi(self)
        self.c = ClientInfo()
        self.addClientBtn.clicked.connect(self.addclient)
        self.voidedClientButton.clicked.connect(self.voidpage)
        self.voidBackBtn.clicked.connect(self.switch_to_ClientsPage)
        self.populate_table()
        # for sidebar menu
        self.pushButton.clicked.connect(self.switch_to_ClientsPage)
        self.pushButton_2.clicked.connect(self.switch_to_SchedulePage)
        self.pushButton_3.clicked.connect(self.switch_to_InventoryPage)
        self.pushButton_4.clicked.connect(self.switch_to_TechnicianPage)
        self.pushButton_5.clicked.connect(self.switch_to_SalesPage)
        self.pushButton_6.clicked.connect(self.switch_to_MaintenancePage)
        self.pushButton_7.clicked.connect(self.switch_to_SMSFormatPage)
        self.pushButton_8.clicked.connect(self.switch_to_HelpPage)
        self.pushButton_9.clicked.connect(self.switch_to_AboutPage)
##########################################################################################

    #for sidebar menu      
    def switch_to_ClientsPage(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_SchedulePage(self):
        self.stackedWidget.setCurrentIndex(1)
    def switch_to_InventoryPage(self):
        self.stackedWidget.setCurrentIndex(2)
    def switch_to_TechnicianPage(self):
        self.stackedWidget.setCurrentIndex(3)
    def switch_to_SalesPage(self):
        self.stackedWidget.setCurrentIndex(4)
    def switch_to_MaintenancePage(self):
        self.stackedWidget.setCurrentIndex(5)
    def switch_to_SMSFormatPage(self):
        self.stackedWidget.setCurrentIndex(6)
    def switch_to_HelpPage(self):
        self.stackedWidget.setCurrentIndex(7)
    def switch_to_AboutPage(self):
        self.stackedWidget.setCurrentIndex(8)
######################################################################

# clientspage
    def populate_table(self):
        #stretch the header
        a = self.clientsTable.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        a.setStretchLastSection(True)
        clients = self.c.select_all_clients()
        if clients:
            self.clientsTable.setRowCount(len(clients))
            self.clientsTable.setColumnCount(5)
            self.clientsTable.setHorizontalHeaderLabels(['Name', 'Phone Number', 'Status', 'Schedule', 'Contract Details'])

            
            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    self.clientsTable.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        else:
            self.clientsTable.setRowCount(0)
            self.clientsTable.setColumnCount(0)

    def void_populate_table(self):
        #stretch the header
        a = self.voidclientsTable.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        a.setStretchLastSection(True)
        clients = self.c.select_all_clients_void()
        if clients:
            self.voidclientsTable.setRowCount(len(clients))
            self.voidclientsTable.setColumnCount(4)
            self.voidclientsTable.setHorizontalHeaderLabels(['Name', 'Phone Number', 'Address', 'Email'])

            
            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    self.voidclientsTable.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        else:
            self.voidclientsTable.setRowCount(0)
            self.voidclientsTable.setColumnCount(0)

    def addclient(self):
        addclient = addClient()
        addclient.exec()
        self.populate_table()
    def voidpage(self):
        self.void_populate_table()
        self.stackedWidget.setCurrentIndex(9)
######################################################################################


app = QApplication([])
window = MainMenu(1)
window.show()
app.exec()