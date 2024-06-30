from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton, QListWidgetItem, QDialog, QVBoxLayout, QFileDialog, QLabel 
from PyQt6 import QtCore, QtGui
from GUI.designMainMenu import Ui_MainWindow
from clientinfo import ClientInfo
from inventory import Inventory
from schedule import Schedule
from sales import Sales
from contract import Contract
from technician import Technician
from user import User
from message import Message
from test import CalendarScheduler
from functools import partial
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
from GUI.designaddadminUI import AddAdmin
from GUI.designaddsmsformatUI import AddSMS
from user import User
from backup_restore import backup_database, restore_database
from GUI.designsmsUI import SMS
import GUI.rc_icons
from pathlib import Path
from designeditadminUI import EditAdmin
from database import *


class MainMenu(QMainWindow, Ui_MainWindow):
    
###########################
    def __init__(self, AdminID, first_Window):
        self.first_window = first_Window
        self.host = 'localhost'
        self.userdb = 'root'
        self.password = '030709'
        self.database = 'mansys'



        
        super().__init__()
        #self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setupUi(self)
        self.adminID = AdminID
        self.user = User()

        # for clients info
        self.c = ClientInfo()
        self.addClientBtn.clicked.connect(self.addclient)
        self.voidedClientButton.clicked.connect(self.voidpage)
        self.voidBackBtn.clicked.connect(self.switch_to_ClientsPage)
        self.populate_table1(self.c.select_all_clients())
        self.stackedWidget.setCurrentIndex(0)
        self.clientSearchBtn.clicked.connect(self.client_search)
        self.voidclientSearchBtn.clicked.connect(self.voidclient_search)

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

        self.inventorysearchBtn.clicked.connect(self.search_inv)

        # for schedulepage
        self.s = Schedule()
        self.addschedBtn.clicked.connect(self.schedAdd)
        self.timetableBtn.clicked.connect(self.timetable)
        self.schedtomBtn.clicked.connect(self.upcomingsched)
        self.schedBackBtn.clicked.connect(self.switch_to_SchedulePage)
        self.sendSMSBtn.clicked.connect(self.sendSMS)
        self.schedulesearchBtn.clicked.connect(self.search_sched)
        self.pushButton_13.clicked.connect(self.switch_to_todayschedPage)
        self.todayschedbackBtn.clicked.connect(self.switch_to_SchedulePage)


        # for salepage
        self.sales= Sales()
        self.addSalesBtn.clicked.connect(lambda: self.addsale(None, None))
        self.salesBtn.clicked.connect(self.switch_to_SalesPage)
        self.revenueBtn.clicked.connect(lambda: self.populate_sale(self.sales.monthly_total_sale(), 0))
        self.pushButton_11.clicked.connect(lambda: self.populate_sale(self.sales.monthly_avg_total_sale(), 1))        
        self.reportBtn.clicked.connect(self.generate_rep)

        self.backBtn.clicked.connect(self.switch_to_ClientsPage)
        self.roundrobinBtn.clicked.connect(self.roundrobin)
        self.pushButton_10.clicked.connect(self.graphforecast)
        self.inventorysearchBtn_2.clicked.connect(self.search_sale)

        #technicianpage
        self.tech = Technician()
        self.addTechnicianBtn.clicked.connect(lambda: self.addtechnician(None))
        self.voidedTechnicianBtn.clicked.connect(self.switch_to_voidtechPage)
        self.techvoidBackBtn.clicked.connect(self.switch_to_TechnicianPage)
        self.itembackBtn.clicked.connect(self.switch_to_TechnicianPage)
        self.servicebackBtn.clicked.connect(self.switch_to_TechnicianPage)
        self.serviceBtn.clicked.connect(self.switch_to_servicePage)
        self.technicianSearch.clicked.connect(self.search_tech)
        #maintenance page
        self.addAdminBtn.clicked.connect(self.addadmin)
        self.userLogBtn.clicked.connect(self.switch_to_userlogPage)
        self.backupBtn.clicked.connect(self.backup)
        self.restoretBn.clicked.connect(self.open_file_dialog)
        self.editAdminBtn.clicked.connect(self.editadmin)

        self.smshelp.clicked.connect(self.open_pdf)
        #SMS page
        self.message = Message()
        self.addSMSBtn.clicked.connect(self.add_sms)
        self.clientSMSBtn.clicked.connect(lambda: self.populate_sms(self.message.show_all_categ('Client')))
        self.techSMSBtn.clicked.connect(lambda: self.populate_sms(self.message.show_all_categ('Technician')))
        self.smsSearchBtn.clicked.connect(self.search_sms)

        #self.message.show_all()
 ##########################################################################################

    #for sidebar menu      
    def switch_to_ClientsPage(self):
        self.stackedWidget.setCurrentIndex(0)
        self.populate_table1(self.c.select_all_clients())
    def switch_to_SchedulePage(self):
        self.stackedWidget.setCurrentIndex(1)
        self.populate_schedule(self.scheduleTable, self.s.view_sched())
    def switch_to_InventoryPage(self):
        self.populate_inventory(self.i.select_inventory(), self.inventoryTable)
        self.stackedWidget.setCurrentIndex(2)
    def switch_to_TechnicianPage(self):
        self.populate_tech(self.tech.select_all_tech())
        self.stackedWidget.setCurrentIndex(3)
    def switch_to_SalesPage(self):
        self.populate_sale(self.sales.view_all_sales(), None)
        self.stackedWidget.setCurrentIndex(4)
    def switch_to_MaintenancePage(self):
        self.stackedWidget.setCurrentIndex(5)
    def switch_to_SMSFormatPage(self):
        self.populate_sms(self.message.show_all())
        self.stackedWidget.setCurrentIndex(6)
    def switch_to_HelpPage(self):
        self.stackedWidget.setCurrentIndex(7)
    def switch_to_AboutPage(self):
        self.stackedWidget.setCurrentIndex(8)
######################################################################
# clientspage
    #may buttons sa table
    
    def populate_table1(self, query):
        # Stretch the header
        a = self.clientsTable.horizontalHeader()
        a.setStretchLastSection(True)
        self.clientsTable.verticalHeader().hide()
        self.clientsTable.setStyleSheet("font-size: 16px; text-align: center;")
        self.contract = Contract()
        clients = query
        if clients:
            self.clientsTable.setRowCount(len(clients))
            self.clientsTable.setColumnCount(8)
            self.clientsTable.setHorizontalHeaderLabels(['Client ID', 'Name', 'Phone Number', 'Address', 'Schedule', 'Contract', ' ', ' '])
            stylesheet = """
                QHeaderView::section {
                    font-weight: bold;
                }
            """
            self.clientsTable.horizontalHeader().setStyleSheet(stylesheet)

            header = self.clientsTable.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

            for row_idx, client in enumerate(clients):
                client_id = client[0]
                for col_idx, item in enumerate(client):
                    items = QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    self.clientsTable.setItem(row_idx, col_idx, items)

                schedview = QPushButton('View')
                schedview.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E3C55C"
                    "}"
                )
                schedview.clicked.connect(partial(self.viewschedule, client_id))
                self.clientsTable.setCellWidget(row_idx, 4, schedview)

                contractview = QPushButton('View' if self.contract.has_a_contract(client_id) else 'Add')
                contractview.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #90CE67"
                    "}"
                )
                contractview.clicked.connect(partial(self.viewcontract if self.contract.has_a_contract(client_id) else self.addContract, client_id))
                self.clientsTable.setCellWidget(row_idx, 5, contractview)

                edit = QPushButton('Edit')
                edit.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #5C7AE3"
                    "}"
                )
                edit.clicked.connect(partial(self.editclient, client_id))
                self.clientsTable.setCellWidget(row_idx, 6, edit)

                delete = QPushButton('Void')
                delete.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E35C5C"
                    "}"
                )
                delete.clicked.connect(lambda _, id = client_id: self.delete(id, self.c.edit_personal_info, 1))
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
        bago = editClients(id, self.adminID)
        bago.exec()
        self.populate_table1(self.c.select_all_clients())
    
    def addContract(self, id):
        addcontract = AddContract(id, None, "Add", self.adminID)
        addcontract.exec()
        self.populate_table1(self.c.select_all_clients())

    def client_search(self):
        search = self.clientSearch.text()
        if search == "":
            self.populate_table1(self.c.select_all_clients())
        else:
            self.populate_table1(self.c.search(search, 0))
#view in contractpage######################################################
    def viewcontract(self, client_id):
        self.stackedWidget.setCurrentIndex(13)
        result = self.c.contract_view(client_id)
        contract_result = self.contract.contract_view(client_id)
        cont_id = self.contract.get_data(client_id, "contract_id")
        hasimg = self.contract.has_img(client_id)
        font = QtGui.QFont()
        font.setPointSize(14)  
        if result:
            self.infolist.clear()
            item = QListWidgetItem()

            item.setFont(font)
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            for row in result:
                item.setText(f"Name: {row[0]}\nPhone: {row[1]}\nAddress: {row[2]}\nEmail: {row[3]}")              
                self.infolist.addItem(item)

        if contract_result:
            self.contractlist.clear()
            item = QListWidgetItem()
            item.setFont(font)
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            for row in contract_result:
                problem, service_type, start_date, end_date, square_meter, unit, price = row
                item.setText(f"Problem: {problem}\n"
                            f"Service Type: {service_type}\n"
                            f"Start Date: {start_date}\n"
                            f"End Date: {end_date}\n"
                            f"Square Meter: {square_meter} \n"
                            f"Unit: {unit}\n"
                            f"Price: {price}")

                self.contractlist.addItem(item)
        self.editcontractBtn.disconnect()
        self.pushButton_14.disconnect()
        if cont_id:
            self.editcontractBtn.clicked.connect(lambda _, id=client_id, cont_id=cont_id[0][0]: 
                                                self.editcontract(id, cont_id))
        if hasimg:
            self.imgholder.clear()
            self.refresh_img(client_id)
            self.pushButton_14.clicked.connect(lambda _, id = client_id: 
                                               self.open_file_dialog_contract(id))
            self.removecontractBtn.clicked.connect(lambda _, id = client_id: 
                                               self.removebtn(id))
            
        
        
    def editcontract(self, client_id, cont_id):
        edit = AddContract(client_id, cont_id, "Edit", self.adminID)
        edit.exec()
        
    def removebtn(self, id):
        self.contract.remove_img(id)
        self.refresh_img(id)

    def open_file_dialog_contract(self, client_id):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Image (*.png *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            filenames = [Path(filename).as_posix() for filename in filenames]  # Convert to POSIX format
            fn = filenames[0]
            print(fn)
            self.contract.insert_image(client_id, fn)
            self.refresh_img(client_id)

    def refresh_img(self, client_id):
        img = self.contract.get_image(client_id)
        if img is not None:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(img)
            # Create a QLabel and set the QPixmap
            self.imgholder.setPixmap(pixmap)
            self.imgholder.setScaledContents(True)
        else: self.imgholder.setText("No Image")

    #for clients and inventory
    def delete(self, id, func, whether):
        noInput = QMessageBox()
        noInput.setWindowTitle("Void")
        noInput.setIcon(QMessageBox.Icon.Warning)
        noInput.setText("Are you sure you want to void?")
        noInput.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        yes = noInput.exec()
        if yes == QMessageBox.StandardButton.Yes:
            func(id, "void", 1)
            if whether == 1:
                self.user.add_backlogs(self.adminID, "Voided Client")
            else:
                self.user.add_backlogs(self.adminID, "Voided Item")
            self.populate_table1(self.c.select_all_clients())
            self.populate_inventory(self.i.choose_category("Chemical"), self.chemicalTable)
            self.populate_inventory(self.i.choose_category("Equipment") , self.equipmentsTable)
            self.populate_inventory(self.i.choose_category("Material"), self.materialsTable)
            self.populate_inventory(self.i.select_inventory(), self.inventoryTable)
        else:
            noInput.close()
        
    def void_populate_table(self, query):
        #stretch the header
        a = self.voidclientsTable.horizontalHeader()
        a.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        a.setStretchLastSection(True)
        self.voidclientsTable.setStyleSheet("font-size: 16px; text-align: center;")
        self.voidclientsTable.verticalHeader().hide()
        clients = query
        if clients:
            self.voidclientsTable.setRowCount(len(clients))
            self.voidclientsTable.setColumnCount(4)
            self.voidclientsTable.setHorizontalHeaderLabels(["ID ",'Name', 'Phone Number', 'Address', 'Email'])
            stylesheet = """
                QHeaderView::section {
                    font-weight: bold;
                }
            """
            self.voidclientsTable.horizontalHeader().setStyleSheet(stylesheet)
            
            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    self.voidclientsTable.setItem(row_idx, col_idx, items)
        else:
            self.voidclientsTable.setRowCount(0)
            self.voidclientsTable.setColumnCount(0)

    def addclient(self):
        addclient = addClient(self.adminID)
        addclient.exec()
        self.populate_table1(self.c.select_all_clients())

    def voidpage(self):
        self.void_populate_table(self.c.select_all_clients_void())
        self.stackedWidget.setCurrentIndex(9)

    def voidclient_search(self):
        search = self.voidclientSearch.text()
        if search == "":
            self.void_populate_table(self.c.select_all_clients_void())
        else:
            self.void_populate_table(self.c.search(search, 1))

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
        tablename.setStyleSheet("font-size: 16px; text-align: center;")
        a.setStretchLastSection(True)
        inventory = type

        if inventory:
            tablename.setRowCount(len(inventory))
            tablename.setColumnCount(8)
            tablename.setHorizontalHeaderLabels(['Item ID','Name', 'Type', 'Quantity', 'Expiration', 'Description',' ',' '])
            stylesheet = """
                QHeaderView::section {
                    font-weight: bold;
                }
            """
            tablename.horizontalHeader().setStyleSheet(stylesheet)
            
            header = tablename.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

            for row_idx, inventorys in enumerate(inventory):
                for col_idx, item in enumerate(inventorys):
                    item_id = inventory[row_idx][0]
                    item_type = inventory[row_idx][2]
                    #tablename.setStyleSheet("font-size: 14px;")
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    tablename.setItem(row_idx, col_idx, items)

                edit = QPushButton('Edit')
                edit.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #5C7AE3"
                    "}"
                )
                edit.clicked.connect(lambda _, id = item_id, type = item_type: self.editInevntory(id, type))
                tablename.setCellWidget(row_idx, 6, edit)

                delete = QPushButton('Void')
                delete.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E35C5C"
                    "}"
                )
                delete.clicked.connect(lambda _, id = item_id: self.delete(id, self.i.edit_inv_info, 0))
                tablename.setCellWidget(row_idx, 7, delete)
        self.label_10.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Inventory</span></p></body></html>"))

    def editInevntory(self, id, type):
        print(id, type)
        edit = Edititem(id, type, self.adminID)
        edit.exec()
        if type == "Chemical": self.populate_inventory(self.i.choose_category("Chemical"), self.chemicalTable)
        elif type == "Equipment": self.populate_inventory(self.i.choose_category("Equipment") , self.equipmentsTable)
        elif type == "Material": self.populate_inventory(self.i.choose_category("Material"), self.materialsTable)
        else: self.populate_inventory(self.i.select_inventory(), self.inventoryTable)

    def addInventory(self, index):
        add = AddItem(index, self.adminID)
        add.exec()
        if index == 0: self.switch_to_ChemicalsPage()
        elif index == 1: self.switch_to_MaterialsPage()
        else: self.switch_to_EquipmentsPage()
    
    def search_inv(self):
        search = self.inventorySearch.text()
        if search == "":
            self.populate_inventory(self.i.select_inventory(), self.inventoryTable)
        else:
            self.populate_inventory(self.i.search(search), self.inventoryTable)
        

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
                stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
                self.inventoryTable.horizontalHeader().setStyleSheet(stylesheet)
            else:
                self.inventoryTable.setHorizontalHeaderLabels(['Delivery ID','Name', 'Quantity', 'Delivery Date', 'Expiration', 'Supplier'])
                stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
                self.inventoryTable.horizontalHeader().setStyleSheet(stylesheet)
            
            for row_idx, sched in enumerate(schedule):
                for col_idx, item in enumerate(sched):
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    self.inventoryTable.setItem(row_idx, col_idx, items)

    def switch_to_delivery(self):
        self.populate_delivery_and_void(self.i.select_all_delivery(), 1)
        self.label_10.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Delivery</span></p></body></html>"))
    
    def switch_to_void(self):
        self.populate_delivery_and_void(self.i.select_inventory_void(),2)
        self.label_10.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Voided Items</span></p></body></html>"))

    def update_delivery(self):
        handol = HandleDelivery(self.adminID)
        handol.exec()

#schedule page######################################################################################################
    def populate_schedule(self, tablename, query):
        a = tablename.horizontalHeader()
        a.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tablename.verticalHeader().hide()
        tablename.setStyleSheet("font-size: 16px; text-align: center;")
        a.setStretchLastSection(True)
        schedule = query
        if schedule:
            tablename.setRowCount(len(schedule))
            tablename.setColumnCount(11)
            tablename.setHorizontalHeaderLabels(['ID', 'Name', 'Type', 'Start Date', 'End Date', 'Time In', 'Time Out', 'Status', 'Technician', ' ', ''])
            stylesheet = """
                QHeaderView::section {
                    font-weight: bold;
                }
            """
            tablename.horizontalHeader().setStyleSheet(stylesheet)

            header = tablename.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

            for row_idx, sched in enumerate(schedule):
                schedule_id = schedule[row_idx][0]
                for col_idx, item in enumerate(sched):
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    tablename.setItem(row_idx, col_idx, items)
                

                if schedule[row_idx][8] is None:
                    assign = QPushButton('Assign')
                    assign.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E3C55C"
                    "}"
                )
                    assign.clicked.connect(lambda _, id=schedule_id: self.assigntech(id))
                    tablename.setCellWidget(row_idx, 8, assign)
                else:
                    tablename.setItem(row_idx, 8, QTableWidgetItem(str(schedule[row_idx][8])))
                edit = QPushButton('Edit')
                edit.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #5C7AE3"
                    "}"
                )
                edit.clicked.connect(lambda _, id=schedule_id: self.schedEdit(id))
                tablename.setCellWidget(row_idx, 9, edit)

                void = QPushButton('Void')
                void.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E35C5C"
                    "}"
                )
                void.clicked.connect(lambda _, id=schedule_id: self.schedVoid(id))
                tablename.setCellWidget(row_idx, 10, void)
        else:
            tablename.setRowCount(0)
            tablename.setColumnCount(0)

    def schedVoid(self, id):
        noInput = QMessageBox()
        noInput.setWindowTitle("Void")
        noInput.setIcon(QMessageBox.Icon.Warning)
        noInput.setText("Are you sure you want to void schedule?")
        noInput.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        yes = noInput.exec()
        if yes == QMessageBox.StandardButton.Yes:
            self.s.edit_schedule_info(id, "void", 1)
            self.s.edit_schedule_info(id, "technician_id", None)
            self.user.add_backlogs(self.adminID, "Voided Item")
            self.populate_schedule(self.scheduleTable, self.s.view_sched())
        else:
            noInput.close()

    def assigntech(self, schedule_id):
        ass = AssignTech(schedule_id, self.adminID)
        ass.exec()
            # Update the schedule data
        for row_idx in range(self.scheduleTable.rowCount()):
            if self.scheduleTable.item(row_idx, 0).text() == str(schedule_id):
                self.scheduleTable.removeCellWidget(row_idx, 8)
                break
        self.populate_schedule(self.scheduleTable, self.s.view_sched())
        self.removebutton_techsched(self.s.show_sched_for_tom(), self.upcomingscheduleTable)

    def schedAdd(self):
        addSchedule = AddSchedule(None, None, self.adminID)
        addSchedule.exec()
        self.populate_schedule(self.scheduleTable, self.s.view_sched())

    def schedEdit(self, id):
        editsched = AddSchedule("Edit", id, self.adminID)
        editsched.exec()
        self.populate_schedule(self.scheduleTable, self.s.view_sched())
        self.populate_schedule(self.upcomingscheduleTable, self.s.show_sched_for_tom())

    def upcomingsched(self):
        self.stackedWidget.setCurrentIndex(17)
        self.populate_schedule(self.upcomingscheduleTable, self.s.show_sched_for_tom())

    def timetable(self):
        mainWin = CalendarScheduler()
        mainWin.exec()

    def roundrobin(self):
        round_robin = self.s.round_robin()
        self.notif(QMessageBox.Icon.Information, round_robin)
        #self.s.view_sched()
        #self.scheduleTable
        self.removebutton_techsched(self.s.view_sched(), self.scheduleTable)
        self.removebutton_techsched(self.s.show_sched_for_tom(), self.upcomingscheduleTable)
        self.user.add_backlogs(self.adminID, "Technician Round Robin")

    def removebutton_techsched(self, query, table):
        s = query 
        for row_idx in range(table.rowCount()):
            schedule_id = s[row_idx][0]
            print(table.rowCount())
            print(schedule_id)
            if table.item(row_idx, 0).text() == str(schedule_id):
                table.removeCellWidget(row_idx, 8)
        self.populate_schedule(table, query)

    def sendSMS(self):
        txtmoko = SMS(self.adminID)
        txtmoko.exec()

    def notif(self, type, message):
        noInput = QMessageBox()
        noInput.setIcon(type)
        noInput.setText(message)
        noInput.exec()

    def search_sched(self):
        search = self.scheduleSearch.text()
        if search == "":
            self.populate_schedule(self.scheduleTable, self.s.view_sched())
        else:
            self.populate_schedule(self.scheduleTable, self.s.search(search))

    def populate_schedule_today(self, tablename, query):
        a = tablename.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        tablename.verticalHeader().hide()
        tablename.setStyleSheet("font-size: 16px; text-align: center;")
        a.setStretchLastSection(True)
        schedule = query
        if schedule:
            tablename.setRowCount(len(schedule))
            tablename.setColumnCount(9)
            tablename.setHorizontalHeaderLabels(['ID', 'Name', 'Schedule Type', 'Start Date', 'End Date', 'Time In', 'Time Out', 'Status', 'Technician'])
            stylesheet = """
                QHeaderView::section {
                    font-weight: bold;
                }
            """
            tablename.horizontalHeader().setStyleSheet(stylesheet)


            header = tablename.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

            for row_idx, sched in enumerate(schedule):
                for col_idx, item in enumerate(sched):
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    tablename.setItem(row_idx, col_idx, items)

    def switch_to_todayschedPage(self):
        self.s.earliest_deadline_first()
        self.populate_schedule_today(self.todayschedTable, self.s.earliest_deadline_first_show())
        self.stackedWidget.setCurrentIndex(19)
        
# sales page ###################################################################################
    def populate_sale(self, query, which):
        a = self.saleTable.horizontalHeader()
        #a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        self.saleTable.verticalHeader().hide()
        self.saleTable.setStyleSheet("font-size: 16px; text-align: center;")
        a.setStretchLastSection(True)  
        
        a.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        sale = query

        if sale:
            self.saleTable.setRowCount(len(sale))
            if which is None:
                self.saleTable.setColumnCount(4)
                self.saleTable.setHorizontalHeaderLabels(['Name','Sale Figure', 'Date', ' '])
                stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
                self.saleTable.horizontalHeader().setStyleSheet(stylesheet)
            elif which == 1:
                self.salesLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Average Sales</span></p><p><br/></p></body></html>"))
                self.saleTable.setColumnCount(3)
                self.saleTable.setHorizontalHeaderLabels(['Year','Month', 'Amount'])
                stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
                self.saleTable.horizontalHeader().setStyleSheet(stylesheet)
            else:
                self.salesLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Revenue</span></p><p><br/></p></body></html>"))
                self.saleTable.setColumnCount(3)
                self.saleTable.setHorizontalHeaderLabels(['Year','Month', 'Amount'])
                stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
                self.saleTable.horizontalHeader().setStyleSheet(stylesheet)
            
            for row_idx, sales in enumerate(sale):
                for col_idx, item in enumerate(sales):
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    self.saleTable.setItem(row_idx, col_idx, items)
                if which is None:
                    sale_id = sale[row_idx][3]
                    #print(sale_id)
                    edit = QPushButton('Edit')
                    edit.setStyleSheet(
                        "QPushButton"
                        "{"
                        "background-color: #5C7AE3"
                        "}"
                    )   
                    edit.clicked.connect(lambda _, id = sale_id: self.addsale("Edit", id))
                    self.saleTable.setCellWidget(row_idx, 3, edit)


    def addsale(self, which, id):
        addsale = AddSales(which, id, self.adminID)
        addsale.exec()
        self.populate_sale(self.sales.view_all_sales(), None)

    def search_sale(self):
        search = self.inventorySearch_2.text()
        if search == "":
            self.populate_sale(self.sales.view_all_sales(), None)
        else:
            self.populate_sale(self.sales.search(search), None)

    def graphforecast(self):
        #self.sales.sale_trend()
        #graph = SaleTrendDialog()
        #graph.exec()
        pass
        
        #print("may error dito")
    
    def generate_rep(self):
        msg = self.sales.generate_report()
        self.user.add_backlogs(self.adminID, "Report Generated")
        self.notif(QMessageBox.Icon.Information, msg)

####### Technician PAGE #############################################################
    def populate_tech(self, query):
        # Stretch the header
        a = self.technicianTable.horizontalHeader()
        a.setStretchLastSection(True)
        self.technicianTable.verticalHeader().hide()
        
        # Set stylesheet for the entire table once
        self.technicianTable.setStyleSheet("font-size: 16px; text-align: center;")

        
        clients = query
        
        if clients:
            self.technicianTable.setRowCount(len(clients))
            self.technicianTable.setColumnCount(8)
            self.technicianTable.setHorizontalHeaderLabels([
                'ID', 'Name', 'Phone Number', 'Address', 'State', 'Assigned Item', '', ''
            ])
            stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
            self.technicianTable.horizontalHeader().setStyleSheet(stylesheet)

            header = self.technicianTable.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    tech_id = clients[row_idx][0]
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    self.technicianTable.setItem(row_idx, col_idx, items)

                # Create buttons
                assignitems = QPushButton('View')
                assignitems.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E3C55C"
                    "}"
                )   
                assignitems.clicked.connect(lambda _, id=tech_id: self.switch_to_assignedItemPage(id))
                self.technicianTable.setCellWidget(row_idx, 5, assignitems)

                edit = QPushButton('Edit')
                edit.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #5C7AE3"
                    "}"
                )   
                edit.clicked.connect(lambda _, id=tech_id: self.edittechnician("Edit", id))
                self.technicianTable.setCellWidget(row_idx, 6, edit)

                void = QPushButton('Void')
                void.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E35C5C"
                    "}"
                )
                void.clicked.connect(lambda _, id=tech_id: self.void(id))
                self.technicianTable.setCellWidget(row_idx, 7, void)
    
    def search_tech(self):
        search = self.TechnicianSearchBtn.text()
        if search == "":
            self.populate_tech(self.tech.select_all_tech())
        else:
            self.populate_tech(self.tech.search(search))

    def populate_tech_void(self, query, which, table):
        # stretch the header
        a = table.horizontalHeader()
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
                stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
                table.horizontalHeader().setStyleSheet(stylesheet)
            else:
                table.setColumnCount(7)
                table.setHorizontalHeaderLabels(['Assigned ID', 'Name', 'Item Name', 'Item Type', 'Quantity', 'Date Acquired', ''])
                stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
                table.horizontalHeader().setStyleSheet(stylesheet)

            for row_idx, client in enumerate(clients):
                for col_idx, item in enumerate(client):
                    techitem_id = clients[row_idx][0]
                    item_id = clients[row_idx][6]
                    quantity = clients[row_idx][4]
                    techid = clients[row_idx][7]
                    items = QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    #items.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    table.setStyleSheet("font-size: 14px; text-align: center;")
                    table.setItem(row_idx, col_idx, items)
                if which is not None:
                    balik = QPushButton('Return')   
                    balik.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E35C5C"
                    "}"
                )
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
            self.user.add_backlogs(self.adminID, "Item Returned")
            self.populate_tech_void(self.tech.show_accounted_item(techid), 1, self.assignitemTable)
        else: noInput.close()
        

    def addtechnician(self, which):
        addtech = AddTechnician(which, None, self.adminID)
        addtech.exec()
        self.populate_tech(self.tech.select_all_tech())
    
    def edittechnician(self, which, id):
        editech = AddTechnician(which, id, self.adminID)
        editech.exec()
        self.populate_tech(self.tech.select_all_tech())

    def void(self, id):
        noInput = QMessageBox()
        noInput.setWindowTitle("Void")
        noInput.setIcon(QMessageBox.Icon.Warning)
        noInput.setText("Are you sure you want to void technician?")
        noInput.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        yes = noInput.exec()
        if yes == QMessageBox.StandardButton.Yes:
            self.tech.edit_technician_info(id, "void", 1)
            self.user.add_backlogs(self.adminID, "Voided Technician")
            self.populate_tech(self.tech.select_all_tech())
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
        window = AssignItem(id, self.adminID)
        window.exec()
        self.populate_tech_void(self.tech.show_accounted_item(id), 1, self.assignitemTable)
        self.assgnBrn.disconnect()

##service page
    def populate_service(self):
        a = self.serviceTable.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        self.serviceTable.verticalHeader().hide()
        self.serviceTable.setStyleSheet("font-size: 16px; text-align: center;")
        a.setStretchLastSection(True)
        header = self.serviceTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        service = self.tech.show_assigned_client()
        if service:
            self.serviceTable.setRowCount(len(service))
            self.serviceTable.setColumnCount(7)
            self.serviceTable.setHorizontalHeaderLabels(['Technician', 'Client', 'Start Date', 'End Date', 'Time In', 'Time Out', 'Report Update'])
            stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
            self.serviceTable.horizontalHeader().setStyleSheet(stylesheet)


            for row_idx, sched in enumerate(service):
                for col_idx, item in enumerate(sched):
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    self.serviceTable.setItem(row_idx, col_idx, items)
                client_id = service[row_idx][7]
                sched_id = service[row_idx][6]
                update = QPushButton('Update')
                update.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E3C55C"
                    "}"
                )   
                update.clicked.connect(lambda _, cid = client_id, sid = sched_id:
                                        self.updatesched(sid, cid))
                self.serviceTable.setCellWidget(row_idx, 6, update)
        else:
            self.serviceTable.setRowCount(0)
            self.serviceTable.setColumnCount(0)

    def switch_to_servicePage(self):
        self.populate_service()
        self.stackedWidget.setCurrentIndex(16)

    def updatesched(self, sched, client):
        print(sched, client)
        noInput = QMessageBox()
        noInput.setWindowTitle("Update")
        noInput.setIcon(QMessageBox.Icon.Information)
        noInput.setText("Are you sure you want to make the client schedule status finished?")
        noInput.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        yes = noInput.exec()
        if yes == QMessageBox.StandardButton.Yes:
            self.s.update_state_when_done(sched, client)
            self.user.add_backlogs(self.adminID, "Updated Schedule")
            self.switch_to_servicePage()
        else: noInput.close()
###### maintenance page #######################################################################3##3
    def populate_userlog(self):
        self.user = User()
        a = self.userlogTable.horizontalHeader()
        a.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.userlogTable.setStyleSheet("font-size: 16px; text-align: center;")
        self.userlogTable.verticalHeader().hide()
        a.setStretchLastSection(True)
        service = self.user.show_userlog()
        self.userlogTable.setColumnCount(4)
        self.userlogTable.setHorizontalHeaderLabels(['ID', 'User ID', 'Activity', 'Date'])
        stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
        self.userlogTable.horizontalHeader().setStyleSheet(stylesheet)
        if service:
            self.userlogTable.setRowCount(len(service))
            for row_idx, sched in enumerate(service):
                for col_idx, item in enumerate(sched):
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    self.userlogTable.setItem(row_idx, col_idx, items)
        else:
            self.userlogTable.setRowCount(0)
            self.userlogTable.setColumnCount(0)

    def switch_to_userlogPage(self):
        self.populate_userlog()
        self.stackedWidget.setCurrentIndex(18)

    def addadmin(self):
        addmin = AddAdmin(self.adminID)
        addmin.exec()
    def editadmin(self):
        edd = EditAdmin(self.adminID)
        edd.exec()
    def backup(self):
        backup_database(self.host, self.userdb, self.password, self.database, "C:/Users/deini/OneDrive/Desktop/backup")

    def open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'C:\Users\deini\OneDrive\Desktop\backup')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("SQL (*.sql)")
        dialog.setViewMode(QFileDialog.ViewMode.List)   
        if dialog.exec():
            filenames = dialog.selectedFiles()
            filenames = [Path(filename) for filename in filenames]
            fn = filenames[0]
            restore_database(self.host, self.userdb, self.password, self.database, fn)
            

############# SMS FORMAT ###################################################################################################
    def populate_sms(self, query):
        
        a = self.smsTable.horizontalHeader()
        a.ResizeMode(QHeaderView.ResizeMode.Stretch)
        self.smsTable.verticalHeader().hide()
        self.smsTable.setStyleSheet("font-size: 16px; text-align: center;")
        a.setStretchLastSection(True)
        sms = query
        self.smsTable.setColumnCount(6)
        self.smsTable.setHorizontalHeaderLabels(['ID', 'Category', 'Message','Title', ' ', ' '])
        header = self.smsTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        stylesheet = """
                    QHeaderView::section {
                        font-weight: bold;
                    }
                """
        self.smsTable.horizontalHeader().setStyleSheet(stylesheet)

        if sms:
            self.smsTable.setRowCount(len(sms))
            for row_idx, sched in enumerate(sms):
                msg_id = sms[row_idx][0]
                for col_idx, item in enumerate(sched):
                    items= QTableWidgetItem(str(item))
                    items.setFlags(items.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable) 
                    self.smsTable.setItem(row_idx, col_idx, items)
                view = QPushButton('View')
                view.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #E3C55C"
                    "}"
                )
                view.clicked.connect(lambda _, msg_id = msg_id: self.view_msg(msg_id))
                self.smsTable.setCellWidget(row_idx, 4, view)
                
                edit = QPushButton('Edit')
                edit.setStyleSheet(
                    "QPushButton"
                    "{"
                    "background-color: #5C7AE3"
                    "}"
                )
                edit.clicked.connect(lambda _, msg_id = msg_id: self.edit_sms(msg_id))
                self.smsTable.setCellWidget(row_idx, 5, edit)                    
        else:
            self.smsTable.setRowCount(0)
            self.smsTable.setColumnCount(0)

    def view_msg(self, id):
        msg = self.message.get_data(id, 'message')
        self.notif(QMessageBox.Icon.NoIcon, msg[0][0])

    def add_sms(self):
        asd = AddSMS(None, None, self.adminID)
        asd.exec()
        self.populate_sms(self.message.show_all())
    
    def edit_sms(self, id):
        edit = AddSMS("Edit", id, self.adminID)
        edit.exec()
        self.populate_sms(self.message.show_all())
    
    def search_sms(self):
        search = self.smsSearch.text()
        if search == "":
            self.populate_sms(self.message.show_all())
        else:
            self.populate_sms(self.message.search(search))
    
    def closeEvent(self, event):
        # Show the first window again when the second window is closed
        self.first_window.show()
        event.accept()
        self.user.add_backlogs(self.adminID, "User Logout")

    def open_pdf(self):
        # Replace with your file path
        pdf_path = "C:/Users/deini/OneDrive/Desktop/SoftEng/Pest-Control-Managment-System/Asset/HomeFix User Manual.pdf"
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(pdf_path))

app = QApplication([])
window = MainMenu("HF00010", app)
window.show()
app.exec()