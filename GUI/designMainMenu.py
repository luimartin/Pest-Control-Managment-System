
from PyQt6 import QtCore, QtGui, QtWidgets
import GUI.rc_icons
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setBaseSize(QtCore.QSize(1024, 768))
        MainWindow.setTabletTracking(False)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.moduleMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.moduleMenu.setGeometry(QtCore.QRect(20, 20, 131, 731))
        self.moduleMenu.setStyleSheet("QWidget{\n"
"background-color:white\n"
"}\n"
"\n"
"QPushButton{\n"
"    height: 100%;\n"
"    width: 100%;\n"
"    border: none\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"         background-color: #D9D9D9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"         background-color: #D9D9D9;\n"
"}\n"
"")
        self.moduleMenu.setObjectName("moduleMenu")
        self.layoutWidget = QtWidgets.QWidget(parent=self.moduleMenu)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 110, 131, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(129, 64))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_7.setMaximumSize(QtCore.QSize(129, 64))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 6, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(129, 63))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(129, 63))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(129, 64))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_9.setMaximumSize(QtCore.QSize(129, 63))
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 8, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(129, 63))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_8.setMaximumSize(QtCore.QSize(129, 63))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 7, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(129, 64))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(160, 20, 841, 731))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("background-color: white;\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.clientsPage = QtWidgets.QWidget()
        self.clientsPage.setStyleSheet("QPushButton{\n"
"    height: 30px;\n"
"    background-color: #D9D9D9;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #A7A6A6;\n"
"    color:white;\n"
"}")
        self.clientsPage.setObjectName("clientsPage")
        self.label_6 = QtWidgets.QLabel(parent=self.clientsPage)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 391, 71))
        self.label_6.setLineWidth(0)
        self.label_6.setScaledContents(False)
        self.label_6.setIndent(3)
        self.label_6.setObjectName("label_6")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.clientsPage)
        self.layoutWidget1.setGeometry(QtCore.QRect(520, 50, 261, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.voidedClientButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.voidedClientButton.setObjectName("voidedClientButton")
        self.horizontalLayout_2.addWidget(self.voidedClientButton)
        self.addClientBtn = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.addClientBtn.setObjectName("addClientBtn")
        self.horizontalLayout_2.addWidget(self.addClientBtn)
        self.clientsTable = QtWidgets.QTableWidget(parent=self.clientsPage)
        self.clientsTable.setGeometry(QtCore.QRect(30, 180, 801, 541))
        self.clientsTable.setObjectName("clientsTable")
        self.clientsTable.setColumnCount(0)
        self.clientsTable.setRowCount(0)
        self.clientSearch = QtWidgets.QLineEdit(parent=self.clientsPage)
        self.clientSearch.setGeometry(QtCore.QRect(30, 130, 801, 31))
        self.clientSearch.setStyleSheet("border: 1px solid black;\n"
"border-radius: 10px;")
        self.clientSearch.setText("")
        self.clientSearch.setObjectName("clientSearch")
        self.label_4 = QtWidgets.QLabel(parent=self.clientsPage)
        self.label_4.setGeometry(QtCore.QRect(790, 136, 20, 20))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/165329.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.clientsPage)
        self.schedulePage = QtWidgets.QWidget()
        self.schedulePage.setObjectName("schedulePage")
        self.label_2 = QtWidgets.QLabel(parent=self.schedulePage)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 71, 41))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.schedulePage)
        self.InventoryPage = QtWidgets.QWidget()
        self.InventoryPage.setStyleSheet("QPushButton{\n"
"    height: 30px;\n"
"    background-color: #D9D9D9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #A7A6A6\n"
"}\n"
"")
        self.InventoryPage.setObjectName("InventoryPage")
        self.label_10 = QtWidgets.QLabel(parent=self.InventoryPage)
        self.label_10.setGeometry(QtCore.QRect(40, 20, 251, 81))
        self.label_10.setLineWidth(0)
        self.label_10.setScaledContents(False)
        self.label_10.setIndent(3)
        self.label_10.setObjectName("label_10")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.InventoryPage)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 170, 801, 541))
        self.tableWidget_2.setLineWidth(-1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.InventoryPage)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 50, 441, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inventoryBtn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.inventoryBtn.setObjectName("inventoryBtn")
        self.horizontalLayout.addWidget(self.inventoryBtn)
        self.chemicalBtn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.chemicalBtn.setObjectName("chemicalBtn")
        self.horizontalLayout.addWidget(self.chemicalBtn)
        self.materialsBtn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.materialsBtn.setStyleSheet("")
        self.materialsBtn.setObjectName("materialsBtn")
        self.horizontalLayout.addWidget(self.materialsBtn)
        self.equipmentBtn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.equipmentBtn.setObjectName("equipmentBtn")
        self.horizontalLayout.addWidget(self.equipmentBtn)
        self.inventorySearch = QtWidgets.QLineEdit(parent=self.InventoryPage)
        self.inventorySearch.setGeometry(QtCore.QRect(20, 124, 801, 31))
        self.inventorySearch.setStyleSheet("border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding-right: 100px")
        self.inventorySearch.setText("")
        self.inventorySearch.setFrame(False)
        self.inventorySearch.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.inventorySearch.setCursorPosition(0)
        self.inventorySearch.setObjectName("inventorySearch")
        self.label_9 = QtWidgets.QLabel(parent=self.InventoryPage)
        self.label_9.setGeometry(QtCore.QRect(790, 130, 20, 20))
        self.label_9.setStyleSheet("")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/165329.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.InventoryPage)
        self.technicianPage = QtWidgets.QWidget()
        self.technicianPage.setObjectName("technicianPage")
        self.label = QtWidgets.QLabel(parent=self.technicianPage)
        self.label.setGeometry(QtCore.QRect(50, 60, 71, 41))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.technicianPage)
        self.salesPage = QtWidgets.QWidget()
        self.salesPage.setObjectName("salesPage")
        self.label_3 = QtWidgets.QLabel(parent=self.salesPage)
        self.label_3.setGeometry(QtCore.QRect(90, 70, 71, 41))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.salesPage)
        self.maintenancePage = QtWidgets.QWidget()
        self.maintenancePage.setStyleSheet("QPushButton{\n"
"    height: 30px;\n"
"    background-color: #D9D9D9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #A7A6A6\n"
"}")
        self.maintenancePage.setObjectName("maintenancePage")
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.maintenancePage)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 160, 791, 551))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.label_11 = QtWidgets.QLabel(parent=self.maintenancePage)
        self.label_11.setGeometry(QtCore.QRect(40, 50, 281, 81))
        self.label_11.setLineWidth(0)
        self.label_11.setScaledContents(False)
        self.label_11.setIndent(3)
        self.label_11.setObjectName("label_11")
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.maintenancePage)
        self.layoutWidget3.setGeometry(QtCore.QRect(550, 100, 241, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(14)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addAdminBtn = QtWidgets.QPushButton(parent=self.layoutWidget3)
        self.addAdminBtn.setObjectName("addAdminBtn")
        self.horizontalLayout_3.addWidget(self.addAdminBtn)
        self.userLogBtn = QtWidgets.QPushButton(parent=self.layoutWidget3)
        self.userLogBtn.setObjectName("userLogBtn")
        self.horizontalLayout_3.addWidget(self.userLogBtn)
        self.layoutWidget.raise_()
        self.tableWidget_3.raise_()
        self.label_11.raise_()
        self.stackedWidget.addWidget(self.maintenancePage)
        self.SMSformatPage = QtWidgets.QWidget()
        self.SMSformatPage.setObjectName("SMSformatPage")
        self.label_8 = QtWidgets.QLabel(parent=self.SMSformatPage)
        self.label_8.setGeometry(QtCore.QRect(70, 50, 71, 41))
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.SMSformatPage)
        self.helpPage = QtWidgets.QWidget()
        self.helpPage.setObjectName("helpPage")
        self.label_5 = QtWidgets.QLabel(parent=self.helpPage)
        self.label_5.setGeometry(QtCore.QRect(60, 50, 71, 41))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.helpPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.label_7 = QtWidgets.QLabel(parent=self.aboutPage)
        self.label_7.setGeometry(QtCore.QRect(80, 50, 71, 41))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.aboutPage)
        self.voidClients = QtWidgets.QWidget()
        self.voidClients.setObjectName("voidClients")
        self.voidclientSearch = QtWidgets.QLineEdit(parent=self.voidClients)
        self.voidclientSearch.setGeometry(QtCore.QRect(20, 130, 801, 31))
        self.voidclientSearch.setStyleSheet("border: 1px solid black;\n"
"border-radius: 10px;")
        self.voidclientSearch.setText("")
        self.voidclientSearch.setObjectName("voidclientSearch")
        self.label_12 = QtWidgets.QLabel(parent=self.voidClients)
        self.label_12.setGeometry(QtCore.QRect(780, 136, 20, 20))
        self.label_12.setStyleSheet("")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/newPrefix/165329.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.voidClients)
        self.label_13.setGeometry(QtCore.QRect(40, 30, 401, 71))
        self.label_13.setLineWidth(0)
        self.label_13.setScaledContents(False)
        self.label_13.setIndent(3)
        self.label_13.setObjectName("label_13")
        self.voidclientsTable = QtWidgets.QTableWidget(parent=self.voidClients)
        self.voidclientsTable.setGeometry(QtCore.QRect(20, 180, 801, 541))
        self.voidclientsTable.setObjectName("voidclientsTable")
        self.voidclientsTable.setColumnCount(0)
        self.voidclientsTable.setRowCount(0)
        self.voidBackBtn = QtWidgets.QPushButton(parent=self.voidClients)
        self.voidBackBtn.setGeometry(QtCore.QRect(680, 70, 101, 38))
        self.voidBackBtn.setStyleSheet("QPushButton{\n"
"border: none;\n"
"background-color: #E35C5C;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(211, 79, 79);\n"
"    \n"
"}")
        self.voidBackBtn.setObjectName("voidBackBtn")
        self.stackedWidget.addWidget(self.voidClients)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.pushButton_3.setText(_translate("MainWindow", "Inventory"))
        self.pushButton_7.setText(_translate("MainWindow", "SMS Format"))
        self.pushButton_4.setText(_translate("MainWindow", "Technician"))
        self.pushButton_6.setText(_translate("MainWindow", "Maintenance"))
        self.pushButton_5.setText(_translate("MainWindow", "Sales"))
        self.pushButton_9.setText(_translate("MainWindow", "About"))
        self.pushButton_2.setText(_translate("MainWindow", "Schedules"))
        self.pushButton_8.setText(_translate("MainWindow", "Help"))
        self.pushButton.setText(_translate("MainWindow", "Clients"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Client Information</span></p></body></html>"))
        self.voidedClientButton.setText(_translate("MainWindow", "Voided Client"))
        self.addClientBtn.setText(_translate("MainWindow", "Add Client"))
        self.label_2.setText(_translate("MainWindow", "schedule"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Inventory</span></p></body></html>"))
        self.inventoryBtn.setText(_translate("MainWindow", "Inventory"))
        self.chemicalBtn.setText(_translate("MainWindow", "Chemical"))
        self.materialsBtn.setText(_translate("MainWindow", "Materials"))
        self.equipmentBtn.setText(_translate("MainWindow", "Equipments"))
        self.inventorySearch.setPlaceholderText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "technician"))
        self.label_3.setText(_translate("MainWindow", "sales"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Maintenance</span></p></body></html>"))
        self.addAdminBtn.setText(_translate("MainWindow", "Add Admin"))
        self.userLogBtn.setText(_translate("MainWindow", "User Logs"))
        self.label_8.setText(_translate("MainWindow", "SMS Format"))
        self.label_5.setText(_translate("MainWindow", "help"))
        self.label_7.setText(_translate("MainWindow", "about"))
        self.voidclientSearch.setPlaceholderText(_translate("MainWindow", "Search"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Void Client</span></p></body></html>"))
        self.voidBackBtn.setText(_translate("MainWindow", "Back"))
