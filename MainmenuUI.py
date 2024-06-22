from PyQt6.QtWidgets import QApplication, QMainWindow,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton, QListWidgetItem
from PyQt6 import QtCore
from GUI.designMainMenu import Ui_MainWindow
from clientinfo import ClientInfo
from inventory import Inventory
from schedule import Schedule
from sales import Sales
from contract import Contract
from technician import Technician
from test import CalendarScheduler
from GUI.addcontractUI import AddContract
from GUI.addclientUI import addClient
from GUI.editclientUI import editClients
from GUI.designadditemUI import AddItem
from GUI.designedititemUI import Edititem
from GUI.designaddschedule import AddSchedule
from GUI.assigntech import AssignTech
from GUI.designhandledeliveryUI import HandleDelivery
from GUI.designaddsalesI import AddSales
from GUI.designaddtechUI import AddTechnician
from GUI.designassignitemUI import AssignItem
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
        self.stackedWidget.setCurrentIndex(0)
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
        self.voiditemBtn.clicked.connect(self.switch_to_void)
        self.deliveryBtn.clicked.connect(self.switch_to_delivery)
        self.newdeliveryBtn.clicked.connect(self.update_delivery)

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
        self.addschedBtn.clicked.connect(self.schedAdd)
        self.scheduleBtn.clicked.connect(self.switch_to_SchedulePage)
        self.timetableBtn.clicked.connect(self.timetable)
        
        # for salepage
        self.sales= Sales()
        self.addSalesBtn.clicked.connect(lambda: self.addsale(None, None))
        self.salesBtn.clicked.connect(self.switch_to_SalesPage)
        self.revenueBtn.clicked.connect(lambda: self.populate_sale(self.sales.monthly_total_sale(), 0))
        self.pushButton_11.clicked.connect(lambda: self.populate_sale(self.sales.monthly_avg_total_sale(), 0))        
        #contractpage
        self.backBtn.clicked.connect(self.switch_to_ClientsPage)
        self.roundrobinBtn.clicked.connect(self.roundrobin)
        self.pushButton_12.clicked.connect(self.graphforecast)

        #technicianpage
        self.addTechnicianBtn.clicked.connect(lambda: self.addtechnician(None))
        self.voidedTechnicianBtn.clicked.connect(self.switch_to_voidtechPage)
        self.techvoidBackBtn.clicked.connect(self.switch_to_TechnicianPage)
        self.itembackBtn.clicked.connect(self.switch_to_TechnicianPage)
 ##########################################################################################

    #for sidebar menu      
    def switch_to_ClientsPage(self):
        self.stackedWidget.setCurrentIndex(0)
        self.populate_table1()
    def switch_to_SchedulePage(self):
        self.stackedWidget.setCurrentIndex(1)
        self.populate_schedule(self.scheduleTable, self.s.view_sched())
    def switch_to_InventoryPage(self):
        self.populate_inventory(self.i.select_inventory(), self.inventoryTable)
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_TechnicianPage(self):
        self.populate_tech()
        self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_SalesPage(self):
        self.populate_sale(self.sales.view_all_sales(), None)
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
        # stretch the header
        a = self.clientsTable.horizontalHeader()
        #a.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.clientsTable.verticalHeader().hide()
        a.setStretchLastSection(True)
        self.contract = Contract()
        clients = self.c.select_all_clients()
        if clients:
            self.clientsTable.setRowCount(len(clients))
            self.clientsTable.setColumnCount(8)
            self.clientsTable.setHorizontalHeaderLabels(['Client ID', 'Name', 'Phone Number', 'Status', 'Schedule', 'Contract Details', ' ', ' '])

            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    client_id = clients[row_idx][0]
                    items = QTableWidgetItem(str(item))
                    #items.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    self.clientsTable.setStyleSheet("font-size: 14px; text-align: center;")
                    self.clientsTable.setItem(row_idx, col_idx, items)

                schedview = QPushButton('View')
                schedview.clicked.connect(lambda _, id=client_id: self.viewschedule(id))
                self.clientsTable.setCellWidget(row_idx, 4, schedview)
                
                # for view client contract and adding if no contract
                if self.contract.has_a_contract(client_id): 
                    contractview = QPushButton('View')
                    contractview.clicked.connect(lambda _, id=client_id: self.viewcontract(id))
                    self.clientsTable.setCellWidget(row_idx, 5, contractview)
                else:
                    contractAdd = QPushButton('Add')
                    contractAdd.clicked.connect(lambda _, id=client_id: self.addContract(id))
                    self.clientsTable.setCellWidget(row_idx, 5, contractAdd)

                edit = QPushButton('Edit')
                edit.clicked.connect(lambda _, id=client_id: self.editclient(id))
                self.clientsTable.setCellWidget(row_idx, 6, edit)

                delete = QPushButton('Void')
                delete.clicked.connect(lambda _, id=client_id: self.delete(id, self.c.edit_personal_info))
                self.clientsTable.setCellWidget(row_idx, 7, delete)
        else:
            self.clientsTable.setRowCount(0)
            self.clientsTable.setColumnCount(0)

    def viewschedule(self, client_id):
        self.pushButton_2.setChecked(True)#toggle button without click
        self.stackedWidget.setCurrentIndex(1)
        #print(client_id)
        self.populate_schedule(self.scheduleTable, self.s.specific_view_sched(client_id))
        
    def editclient(self, id):
        bago = editClients(id)
        bago.exec()
        self.populate_table1()
    
    def addContract(self, id):
        addcontract = AddContract(id, None, "Add")
        addcontract.exec()

#view in contractpage######################################################
    def viewcontract(self, client_id):
        self.stackedWidget.setCurrentIndex(13)
        result = self.c.contract_view(client_id)
        contract_result = self.contract.contract_view(client_id)
        cont_id = self.contract.get_data(client_id, "contract_id")
        if result:
            self.infolist.clear()
            for row in result:
                item = QListWidgetItem()
                item.setText(f"Name: {row[0]}\nPhone: {row[1]}\nAddress: {row[2]}\nEmail: {row[3]}")
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                self.infolist.addItem(item)

        if contract_result:
            self.contractlist.clear()
            for row in contract_result:
                problem, service_type, start_date, end_date, square_meter, unit, price = row
                
                item = QListWidgetItem()
                item.setText(f"Problem: {problem}\n"
                            f"Service Type: {service_type}\n"
                            f"Start Date: {start_date}\n"
                            f"End Date: {end_date}\n"
                            f"Square Meter: {square_meter} \n"
                            f"Unit: {unit}\n"
                            f"Price: {price}")
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                self.contractlist.addItem(item)
        self.editcontractBtn.disconnect()
        if cont_id:
            self.editcontractBtn.clicked.connect(lambda _, id=client_id, cont_id=cont_id[0][0]: 
                                                self.editcontract(id, cont_id))
        
        
    def editcontract(self, client_id, cont_id):
        edit = AddContract(client_id, cont_id, "Edit")
        edit.exec()

    #for clients and inventory
    def delete(self, id, func):
        noInput = QMessageBox()
        noInput.setWindowTitle("Void")
        noInput.setIcon(QMessageBox.Icon.Warning)
        noInput.setText("Are you sure you want to void?")
        noInput.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        yes = noInput.exec()
        if yes == QMessageBox.StandardButton.Yes:
            func(id, "void", 1)
            self.populate_table1()
            self.populate_inventory(self.i.choose_category("Chemical"), self.chemicalTable)
            self.populate_inventory(self.i.choose_category("Equipment") , self.equipmentsTable)
            self.populate_inventory(self.i.choose_category("Material"), self.materialsTable)
            self.populate_inventory(self.i.select_inventory(), self.inventoryTable)
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


##################################################################################################
#Inventory Page
    def switch_to_ChemicalsPage(self):
            self.populate_inventory(self.i.choose_category("Chemical"), self.chemicalTable)
            self.stackedWidget.setCurrentIndex(10)
            
    def switch_to_EquipmentsPage(self):
            self.populate_inventory(self.i.choose_category("Equipment") , self.equipmentsTable)
            self.stackedWidget.setCurrentIndex(11)
    def switch_to_MaterialsPage(self):
            self.populate_inventory(self.i.choose_category("Material"), self.materialsTable)
            self.stackedWidget.setCurrentIndex(12)
           
    def populate_inventory(self, type, tablename):
        a = tablename.horizontalHeader()
        #a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        tablename.verticalHeader().hide()
        a.setStretchLastSection(True)
        inventory = type

        if inventory:
            tablename.setRowCount(len(inventory))
            tablename.setColumnCount(8)
            tablename.setHorizontalHeaderLabels(['Item ID','Name', 'Type', 'Quantity', 'Expiration', 'Description',' ',' '])
            
            for row_idx, inventorys in enumerate(inventory):
                for col_idx, item in enumerate(inventorys):
                    item_id = inventory[row_idx][0]
                    item_type = inventory[row_idx][2]
                    #tablename.setStyleSheet("font-size: 14px;")
                    tablename.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

                edit = QPushButton('Edit')
                edit.clicked.connect(lambda _, id = item_id, type = item_type: self.editInevntory(id, type))
                tablename.setCellWidget(row_idx, 6, edit)

                delete = QPushButton('Void')
                delete.clicked.connect(lambda _, id = item_id: self.delete(id, self.i.edit_inv_info))
                tablename.setCellWidget(row_idx, 7, delete)
        self.label_10.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Inventory</span></p></body></html>"))

    def editInevntory(self, id, type):
        print(id, type)
        edit = Edititem(id, type)
        edit.exec()
        if type == "Chemical": self.populate_inventory(self.i.choose_category("Chemical"), self.chemicalTable)
        elif type == "Equipment": self.populate_inventory(self.i.choose_category("Equipment") , self.equipmentsTable)
        elif type == "Material": self.populate_inventory(self.i.choose_category("Material"), self.materialsTable)
        else: self.populate_inventory(self.i.select_inventory(), self.inventoryTable)

    def addInventory(self, index):
        add = AddItem(index)
        add.exec()
        if index == 0: self.switch_to_ChemicalsPage()
        elif index == 1: self.switch_to_MaterialsPage()
        else: self.switch_to_EquipmentsPage()

    def populate_delivery_and_void(self, query, categ):
        a = self.inventoryTable.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        self.inventoryTable.verticalHeader().hide()
        a.setStretchLastSection(True)
        schedule = query
        if schedule:
            self.inventoryTable.setRowCount(len(schedule))
            self.inventoryTable.setColumnCount(6)
            if categ == 2:
                self.inventoryTable.setHorizontalHeaderLabels(['Item ID','Name', 'Type', 'Quantity', 'Expiration', 'Description'])
            else:
                self.inventoryTable.setHorizontalHeaderLabels(['Delivery ID','Name', 'Quantity', 'Delivery Date', 'Expiration', 'Supplier'])
            for row_idx, sched in enumerate(schedule):
                for col_idx, item in enumerate(sched):
                    self.inventoryTable.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

    def switch_to_delivery(self):
        self.populate_delivery_and_void(self.i.select_all_delivery(), 1)
        self.label_10.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Delivery</span></p></body></html>"))
    
    def switch_to_void(self):
        self.populate_delivery_and_void(self.i.select_inventory_void(),2)
        self.label_10.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Voided Items</span></p></body></html>"))

    def update_delivery(self):
        handol = HandleDelivery()
        handol.exec()

#schedule page######################################################################################################
    def populate_schedule(self, tablename, query):
        a = tablename.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        tablename.verticalHeader().hide()
        a.setStretchLastSection(True)
        schedule = query
        if schedule:
            tablename.setRowCount(len(schedule))
            tablename.setColumnCount(10)
            tablename.setHorizontalHeaderLabels(['ID', 'Name', 'Schedule Type', 'Start Date', 'End Date', 'Time In', 'Time Out', 'Status', 'Technician', ' '])

            for row_idx, sched in enumerate(schedule):
                for col_idx, item in enumerate(sched):
                    tablename.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
                schedule_id = schedule[row_idx][0]

                if schedule[row_idx][8] is None:
                    assign = QPushButton('Assign')
                    assign.clicked.connect(lambda _, id=schedule_id: self.assigntech(id))
                    tablename.setCellWidget(row_idx, 8, assign)
                else:
                    tablename.setItem(row_idx, 8, QTableWidgetItem(str(schedule[row_idx][8])))
                edit = QPushButton('Edit')
                edit.clicked.connect(lambda _, id=schedule_id: self.schedEdit(id))
                tablename.setCellWidget(row_idx, 9, edit)
        else:
            tablename.setRowCount(0)
            tablename.setColumnCount(0)

    def assigntech(self, schedule_id):
        ass = AssignTech(schedule_id)
        ass.exec()
            # Update the schedule data
        for row_idx in range(self.scheduleTable.rowCount()):
            if self.scheduleTable.item(row_idx, 0).text() == str(schedule_id):
                self.scheduleTable.removeCellWidget(row_idx, 8)
                break
        self.populate_schedule(self.scheduleTable, self.s.view_sched())

    def schedAdd(self):
        addSchedule = AddSchedule(None, None)
        addSchedule.exec()
        self.populate_schedule(self.scheduleTable, self.s.view_sched())

    def schedEdit(self, id):
        editsched = AddSchedule("Edit", id)
        editsched.exec()
        self.populate_schedule(self.scheduleTable, self.s.view_sched())
    def timetable(self):
        mainWin = CalendarScheduler()
        mainWin.exec()

    def roundrobin(self):
        round_robin = self.s.round_robin()
        self.notif(QMessageBox.Icon.Information, round_robin)
        s = self.s.view_sched()
        for row_idx in range(self.scheduleTable.rowCount()):
            schedule_id = s[row_idx][0]
            print(self.scheduleTable.rowCount())
            print(schedule_id)
            if self.scheduleTable.item(row_idx, 0).text() == str(schedule_id):
                self.scheduleTable.removeCellWidget(row_idx, 8)
        self.populate_schedule(self.scheduleTable, self.s.view_sched())

    def notif(self, type, message):
        noInput = QMessageBox()
        noInput.setIcon(type)
        noInput.setText(message)
        noInput.exec()

# sales page ###################################################################################
    def populate_sale(self, query, which):
        a = self.saleTable.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        self.saleTable.verticalHeader().hide()
        a.setStretchLastSection(True)  
        sale = query

        if sale:
            self.saleTable.setRowCount(len(sale))
            if which is None:
                self.saleTable.setColumnCount(4)
                self.saleTable.setHorizontalHeaderLabels(['Name','Sale Figure', 'Date', ' '])
            else:
                self.saleTable.setColumnCount(3)
                self.saleTable.setHorizontalHeaderLabels(['Year','Month', 'Amount'])
            
            for row_idx, sales in enumerate(sale):
                for col_idx, item in enumerate(sales):
                    self.saleTable.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
                if which is None:
                    sale_id = sale[row_idx][3]
                    #print(sale_id)
                    edit = QPushButton('Edit')
                    edit.clicked.connect(lambda _, id = sale_id: self.addsale("Edit", id))
                    self.saleTable.setCellWidget(row_idx, 3, edit)


    def addsale(self, which, id):
        addsale = AddSales(which, id)
        addsale.exec()
        self.populate_sale(self.sales.view_all_sales(), None)

    def graphforecast(self):
        #graph = SaleTrendDialog()
        #graph.exec()
        print("may error dito")

####### Technician PAGE #############################################################
    def populate_tech(self):
        # stretch the header
        a = self.technicianTable.horizontalHeader()
        #a.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.technicianTable.verticalHeader().hide()
        a.setStretchLastSection(True)
        self.tech = Technician()
        clients = self.tech.select_all_tech()
        if clients:
            self.technicianTable.setRowCount(len(clients))
            self.technicianTable.setColumnCount(8)
            self.technicianTable.setHorizontalHeaderLabels(['ID', 'Name', 'Phone Number', 'Address', 'State' ,'Assigned Item', '', ''])

            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    tech_id = clients[row_idx][0]
                    items = QTableWidgetItem(str(item))
                    #items.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    self.technicianTable.setStyleSheet("font-size: 14px; text-align: center;")
                    self.technicianTable.setItem(row_idx, col_idx, items)

                assignitems = QPushButton('View')
                assignitems.clicked.connect(lambda _, id=tech_id: self.switch_to_assignedItemPage(id))
                self.technicianTable.setCellWidget(row_idx, 5, assignitems)

                edit = QPushButton('Edit')
                edit.clicked.connect(lambda _, id=tech_id: self.edittechnician("Edit",id))
                self.technicianTable.setCellWidget(row_idx, 6, edit)

                void = QPushButton('Void')
                void.clicked.connect(lambda _, id=tech_id: self.delete(id))
                self.technicianTable.setCellWidget(row_idx, 7, void)
            #self.editcontractBtn.disconnect()

    def populate_tech_void(self, query, which, table):
        # stretch the header
        a = self.technicianTable.horizontalHeader()
        #a.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().hide()
        a.setStretchLastSection(True)
        self.tech = Technician()
        clients = query
        if clients:
            table.setRowCount(len(clients))
            if which is None:
                table.setColumnCount(4)
                table.setHorizontalHeaderLabels(['ID', 'Name', 'Phone Number', 'Address'])
            else:
                table.setColumnCount(7)
                table.setHorizontalHeaderLabels(['Assigned ID', 'Name', 'Item Name', 'Item Type', 'Quantity', 'Date Acquired', ''])


            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    techitem_id = clients[row_idx][0]
                    item_id = clients[row_idx][6]
                    quantity = clients[row_idx][4]
                    techid = clients[row_idx][7]
                    items = QTableWidgetItem(str(item))
                    #items.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    table.setStyleSheet("font-size: 14px; text-align: center;")
                    table.setItem(row_idx, col_idx, items)
                if which is not None:
                    balik = QPushButton('Return')
                    balik.clicked.connect(lambda _, id=techitem_id, item = item_id
                                          , quant = quantity: self.returnitem(id, item, quant, techid))
                    table.setCellWidget(row_idx, 6, balik)

        else:
            table.setRowCount(0)
            table.setColumnCount(0)
        
    def returnitem(self,techitem_id, item_id, quantity, techid):
        print( techitem_id, item_id, quantity)
        noInput = QMessageBox()
        noInput.setWindowTitle("Void")
        noInput.setIcon(QMessageBox.Icon.Warning)
        noInput.setText("Are you sure you want to return item in inventory?")
        noInput.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        yes = noInput.exec()
        if yes == QMessageBox.StandardButton.Yes:
            self.tech.return_item(techitem_id, item_id, quantity)
            self.populate_tech_void(self.tech.show_accounted_item(techid), 1, self.assignitemTable)
        else: noInput.close()
        
        


    def addtechnician(self, which):
        addtech = AddTechnician(which, None)
        addtech.exec()
        self.populate_tech()
    
    def edittechnician(self, which, id):
        editech = AddTechnician(which, id)
        editech.exec()
        self.populate_tech()

    def delete(self, id):
        noInput = QMessageBox()
        noInput.setWindowTitle("Void")
        noInput.setIcon(QMessageBox.Icon.Warning)
        noInput.setText("Are you sure you want to void technician?")
        noInput.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        yes = noInput.exec()
        if yes == QMessageBox.StandardButton.Yes:
            self.tech.edit_technician_info(id, "void", 1)
            self.populate_tech()
        else: noInput.close()

#### tech item assign
    def switch_to_voidtechPage(self):
        self.populate_tech_void(self.tech.select_all_tech_void(), None, self.voidtechnicianTable)
        self.stackedWidget.setCurrentIndex(14)

    def switch_to_assignedItemPage(self, id):
        self.populate_tech_void(self.tech.show_accounted_item(id), 1, self.assignitemTable)
        self.stackedWidget.setCurrentIndex(15)
        self.assgnBrn.clicked.connect(lambda: self.itemassign(id))
        

    def itemassign(self, id):
        print(id, "Rawr")
        window = AssignItem(id)
        window.exec()
        self.populate_tech_void(self.tech.show_accounted_item(id), 1, self.assignitemTable)
        self.assgnBrn.disconnect()



app = QApplication([])
window = MainMenu(1)
window.show()
app.exec()