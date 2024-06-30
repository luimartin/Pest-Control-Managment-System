from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 364)
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 49, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_16 = QtWidgets.QLabel(parent=Dialog)
        self.label_16.setGeometry(QtCore.QRect(30, 10, 251, 81))
        self.label_16.setLineWidth(0)
        self.label_16.setScaledContents(False)
        self.label_16.setIndent(3)
        self.label_16.setObjectName("label_16")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(221, 290, 91, 41))
        self.cancelBtn.setStyleSheet("QPushButton{\n"
"border: none;\n"
"background-color: #E35C5C;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(211, 79, 79);\n"
"    \n"
"}")
        self.cancelBtn.setObjectName("cancelBtn")
        self.addBtn = QtWidgets.QPushButton(parent=Dialog)
        self.addBtn.setGeometry(QtCore.QRect(330, 290, 101, 41))
        self.addBtn.setStyleSheet("QPushButton{border: none;\n"
"background-color: rgb(0, 255, 0);\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #5CE371\n"
"}")
        self.addBtn.setObjectName("addBtn")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 100, 381, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt;\">Add Sales</span></p></body></html>"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.addBtn.setText(_translate("Dialog", "Add "))
        self.label.setText(_translate("Dialog", "Client Name"))
        self.label_2.setText(_translate("Dialog", "Amount in Pesos"))
        self.label_3.setText(_translate("Dialog", "Date"))
# may runner dito
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from clientinfo import ClientInfo
from sales import Sales
from user import User
class AddSales(QDialog, Ui_Dialog):
    
    def __init__(self, which, id, admin):
        super().__init__()
        self.setupUi(self)
        self.c = ClientInfo()
        self.s = Sales()
        self.u = User()
        self.admin = admin
        self.which = which
        self.sale_id = id
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.lineEdit.setValidator(QtGui.QDoubleValidator(0.0, 5.0, 4))
        data = self.c.select_all_clients()
        for client_id, name, _ ,_  in data:
            self.comboBox.addItem(name, client_id)

        self.addBtn.clicked.connect(self.add)
        self.cancelBtn.clicked.connect(lambda: self.close())

        if which == "Edit":
            print(self.sale_id)
            self.comboBox.setEnabled(False)
            placeholder = self.s.view_specific_sales(id)
            self.comboBox.setCurrentText(str(placeholder[0][0]))
            self.lineEdit.setText(str(placeholder[0][1]))
            self.dateEdit.setDate(QtCore.QDate.fromString(str(placeholder[0][2]), "yyyy-MM-dd"))
            #print(self.comboBox.currentData())
            
    def add(self):
        id = self.comboBox.currentData()
        amount = self.lineEdit.text()
        date = self.dateEdit.date()
        date = date.toString("yyyy-MM-dd")
        #print(date, id, amount)
        if self.which == "Edit":
            self.s.edit_sale_info(self.sale_id, "figure", amount)
            self.s.edit_sale_info(self.sale_id, "sale_date", date)
            self.notif("Sales Edited",  QMessageBox.Icon.Information)
            self.u.add_backlogs(self.admin, "Edited Sales")
            self.close()
        else:
            if amount == "":
                self.notif("Invalid Input", QMessageBox.Icon.Warning)
            else: 
                self.s.add_sale(id, amount, date)
                self.u.add_backlogs(self.admin, "Edited Sales")
                self.notif("Sales Added", QMessageBox.Icon.Information)
                self.u.add_backlogs(self.admin, "Added Sales")
                self.close()

    def notif(self, message, icon):
        noInput = QMessageBox()
        noInput.setIcon(icon)
        noInput.setText(message)
        noInput.exec()

