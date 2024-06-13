from PyQt6.QtWidgets import QApplication, QMainWindow,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton
from PyQt6 import QtCore
from GUI.designMainMenu import Ui_MainWindow
from clientinfo import ClientInfo
from inventory import Inventory
from schedule import Schedule
from GUI.addclientUI import addClient
from GUI.editclientUI import editClients
from GUI.designadditemUI import AddItem
from GUI.designedititemUI import Edititem
class MainMenu(QMainWindow, Ui_MainWindow):
    #move frameless window
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
        self.dragPos = event.globalPosition().toPoint()
        event.accept()
###########################
    def __init__(self, AdminID):
        
        super().__init__()
        #self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setupUi(self)
        # for clients info
        self.c = ClientInfo()
        self.addClientBtn.clicked.connect(self.addclient)
        self.voidedClientButton.clicked.connect(self.voidpage)
        self.voidBackBtn.clicked.connect(self.switch_to_ClientsPage)
        self.populate_table1()

        # for sidebar menu
        self.pushButton.setChecked(True)#toggle button without click
        self.pushButton.clicked.connect(self.switch_to_ClientsPage)
        self.pushButton_2.clicked.connect(self.switch_to_SchedulePage)
        self.pushButton_3.clicked.connect(self.switch_to_InventoryPage)
        self.pushButton_4.clicked.connect(self.switch_to_TechnicianPage)
        self.pushButton_5.clicked.connect(self.switch_to_SalesPage)
        self.pushButton_6.clicked.connect(self.switch_to_MaintenancePage)
        self.pushButton_7.clicked.connect(self.switch_to_SMSFormatPage)
        self.pushButton_8.clicked.connect(self.switch_to_HelpPage)
        self.pushButton_9.clicked.connect(self.switch_to_AboutPage)
        self.pushButton_10.clicked.connect(lambda: self.close())
        
        #inventorypage
        self.i = Inventory()
        #self.populate_inventory(0, self.inventoryTable)
        self.chemicalBtn.clicked.connect(self.switch_to_ChemicalsPage)
        self.chemchemicalBtn.clicked.connect(self.switch_to_ChemicalsPage)
        self.matchemicalBtn.clicked.connect(self.switch_to_ChemicalsPage)
        self.eqchemicalBtn.clicked.connect(self.switch_to_ChemicalsPage)

        self.cheminventoryBtn.clicked.connect(self.switch_to_InventoryPage)
        self.eqinventoryBtn.clicked.connect(self.switch_to_InventoryPage)
        self.matinventoryBtn.clicked.connect(self.switch_to_InventoryPage)
        self.inventoryBtn.clicked.connect(self.switch_to_InventoryPage)

        self.chemequipmentBtn.clicked.connect(self.switch_to_EquipmentsPage)
        self.matequipmentBtn.clicked.connect(self.switch_to_EquipmentsPage)
        self.eqequipmentBtn.clicked.connect(self.switch_to_EquipmentsPage)
        self.equipmentBtn.clicked.connect(self.switch_to_EquipmentsPage)

        self.chemmaterialsBtn.clicked.connect(self.switch_to_MaterialsPage)
        self.matmaterialsBtn.clicked.connect(self.switch_to_MaterialsPage)
        self.eqmaterialsBtn.clicked.connect(self.switch_to_MaterialsPage)
        self.materialsBtn.clicked.connect(self.switch_to_MaterialsPage)

        self.equipmentAddBtn.clicked.connect(lambda: self.addInventory(2))
        self.materialsAddBtn.clicked.connect(lambda: self.addInventory(1))
        self.chemicalsAddBtn.clicked.connect(lambda: self.addInventory(0))

        # for schedulepage
        self.s = Schedule()
 ##########################################################################################

    #for sidebar menu      
    def switch_to_ClientsPage(self):
        self.stackedWidget.setCurrentIndex(0)
        self.populate_table1()
    def switch_to_SchedulePage(self):
        self.stackedWidget.setCurrentIndex(1)
        self.populate_schedule(self.scheduleTable)
    def switch_to_InventoryPage(self):
        self.reload = self.populate_inventory(0, self.inventoryTable)
        self.reload
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
    #may buttons sa table
    def populate_table1(self):
        #stretch the header
        a = self.clientsTable.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        self.clientsTable.verticalHeader().hide()
        a.setStretchLastSection(True)  
        clients = self.c.select_all_clients()
        if clients:
            self.clientsTable.setRowCount(len(clients))
            self.clientsTable.setColumnCount(8)
            self.clientsTable.setHorizontalHeaderLabels(['Client ID','Name', 'Phone Number', 'Status', 'Schedule', 'Contract Details',' ',' '])
            
            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    #print(type(row_idx))
                    #print(clients[row_idx][0])
                    client_id = clients[row_idx][0]
                    #print(client_id)
                    self.clientsTable.setStyleSheet("font-size: 14px;")
                    self.clientsTable.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

                schedview = QPushButton('View')
                schedview.clicked.connect(lambda _, id=client_id: self.viewschedule(id))
                self.clientsTable.setCellWidget(row_idx, 4, schedview)

                contractview = QPushButton('View')
                #button.clicked.connect(lambda _, id=client_id: self.viewschedule(id))
                self.clientsTable.setCellWidget(row_idx, 5, contractview)

                edit = QPushButton('Edit')
                edit.clicked.connect(lambda _, id=client_id: self.editclient(id))
                self.clientsTable.setCellWidget(row_idx, 6, edit)

                delete = QPushButton('Delete')
                delete.clicked.connect(lambda _, id=client_id: self.delete(id, self.c.edit_personal_info))
                self.clientsTable.setCellWidget(row_idx, 7, delete)
        else:
            self.clientsTable.setRowCount(0)
            self.clientsTable.setColumnCount(0)

    def viewschedule(self, client_id):
        print("tite", client_id)
        self.pushButton_2.setChecked(True)#toggle button without click
        self.switch_to_SchedulePage()
        
    def editclient(self, id):
        bago = editClients(id)
        bago.exec()
        self.populate_table1()
    
    #for clients and inventory
    def delete(self, id, func):
        noInput = QMessageBox()
        noInput.setWindowTitle("Error")
        noInput.setIcon(QMessageBox.Icon.Warning)
        noInput.setText("Are you sure you want to delete ?")
        noInput.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        yes = noInput.exec()
        if yes == QMessageBox.StandardButton.Yes:
            func(id, "void", 1)
            self.populate_table1()
            self.populate_inventory(1, self.chemicalTable)
            self.populate_inventory(3, self.equipmentsTable)
            self.populate_inventory(2, self.materialsTable)
            self.populate_inventory(0, self.inventoryTable)
        else:
            noInput.close()


        
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
        self.populate_table1()
    def voidpage(self):
        self.void_populate_table()
        self.stackedWidget.setCurrentIndex(9)
######################################################################################
#Inventory Page
    def switch_to_ChemicalsPage(self):
            self.populate_inventory(1, self.chemicalTable)
            self.stackedWidget.setCurrentIndex(10)
            
    def switch_to_EquipmentsPage(self):
            self.populate_inventory(3, self.equipmentsTable)
            self.stackedWidget.setCurrentIndex(11)
    def switch_to_MaterialsPage(self):
            self.populate_inventory(2, self.materialsTable)
            self.stackedWidget.setCurrentIndex(12)
           
    def populate_inventory(self, type, tablename):
        a = tablename.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        tablename.verticalHeader().hide()
        a.setStretchLastSection(True)  
        if type == 0: inventory = self.i.select_inventory()
        elif type == 1: inventory = self.i.choose_category("Chemical")
        elif type == 2: inventory = self.i.choose_category("Material")
        else: inventory = self.i.choose_category("Equipment") 

        if inventory:
            tablename.setRowCount(len(inventory))
            tablename.setColumnCount(8)
            tablename.setHorizontalHeaderLabels(['Item ID','Name', 'Type', 'Quantity', 'Expiration', 'Description',' ',' '])
            
            for row_idx, inventorys in enumerate(inventory):
                for col_idx, item in enumerate(inventorys):
                    item_id = inventory[row_idx][0]
                    item_type = inventory[row_idx][2]
                    tablename.setStyleSheet("font-size: 14px;")
                    tablename.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

                edit = QPushButton('Edit')
                edit.clicked.connect(lambda _, id = item_id, type = item_type: self.editInevntory(id, type))
                tablename.setCellWidget(row_idx, 6, edit)

                delete = QPushButton('Delete')
                delete.clicked.connect(lambda _, id = item_id: self.delete(id, self.i.edit_inv_info))
                tablename.setCellWidget(row_idx, 7, delete)

    def editInevntory(self, id, type):
        print(id, type)
        edit = Edititem(id, type)
        edit.exec()
        if type == "Chemical": self.populate_inventory(1, self.chemicalTable)
        elif type == "Equipment": self.populate_inventory(3, self.equipmentsTable)
        elif type == "Material": self.populate_inventory(2, self.materialsTable)
        else: self.populate_inventory(0, self.inventoryTable)

    def addInventory(self, index):
        print(index)
        add = AddItem(index)
        add.exec()
        if index == 0: self.switch_to_ChemicalsPage()
        elif index == 1: self.switch_to_MaterialsPage()
        else: self.switch_to_EquipmentsPage()

#schedule page
    def populate_schedule(self, tablename):
        a = tablename.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        tablename.verticalHeader().hide()
        a.setStretchLastSection(True)  
        schedule = self.s.view_sched()

        if schedule:
            tablename.setRowCount(len(schedule))
            tablename.setColumnCount(8)
            tablename.setHorizontalHeaderLabels(['Name','Schedule Type', 'Start Date', 'End Date', 'Time In', 'Time Out','Status','Technician'])
            
            for row_idx, sched in enumerate(schedule):
                for col_idx, item in enumerate(sched):
                    tablename.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
app = QApplication([])
window = MainMenu(1)
window.show()
app.exec()