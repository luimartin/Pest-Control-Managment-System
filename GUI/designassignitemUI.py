from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(483, 408)
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.label_7.setObjectName("label_7")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(250, 350, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.submitBtn = QtWidgets.QPushButton(parent=Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(370, 350, 75, 24))
        self.submitBtn.setObjectName("submitBtn")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 80, 411, 231))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(17)
        self.gridLayout.setVerticalSpacing(38)
        self.gridLayout.setObjectName("gridLayout")
        self.nameInput = QtWidgets.QLineEdit(parent=self.widget)
        self.nameInput.setObjectName("nameInput")
        self.gridLayout.addWidget(self.nameInput, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.quantityInput = QtWidgets.QLineEdit(parent=self.widget)
        self.quantityInput.setObjectName("quantityInput")
        self.gridLayout.addWidget(self.quantityInput, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chemBtn = QtWidgets.QPushButton(parent=self.widget)
        self.chemBtn.setObjectName("chemBtn")
        self.horizontalLayout.addWidget(self.chemBtn)
        self.matBtm = QtWidgets.QPushButton(parent=self.widget)
        self.matBtm.setObjectName("matBtm")
        self.horizontalLayout.addWidget(self.matBtm)
        self.equipBtn = QtWidgets.QPushButton(parent=self.widget)
        self.equipBtn.setObjectName("equipBtn")
        self.horizontalLayout.addWidget(self.equipBtn)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Assign Item</span></p></body></html>"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.submitBtn.setText(_translate("Dialog", "Submit"))
        self.label_3.setText(_translate("Dialog", "Select Item: "))
        self.chemBtn.setText(_translate("Dialog", "Chemical"))
        self.matBtm.setText(_translate("Dialog", "Material"))
        self.equipBtn.setText(_translate("Dialog", "Equipments"))
        self.pushButton_4.setText(_translate("Dialog", "All"))
        self.label_4.setText(_translate("Dialog", "Quantity: "))
        self.label.setText(_translate("Dialog", "Technician Name: "))

from PyQt6.QtWidgets import QDialog,QMessageBox, QApplication

from technician import Technician
from inventory import Inventory
# if edit tangalin yung runner dito
class AssignItem(QDialog, Ui_Dialog):
    def __init__(self, tech_id):
        super().__init__()
        self.setupUi(self)
        self.tech = Technician()
        self.inv = Inventory()
        #self.dateEdit.setVisible(False)
        #self.label_2.setVisible(False)
        self.tech_id = tech_id
        name = self.tech.get_data(tech_id, 'concat(TECHNICIAN.first_name, " ", TECHNICIAN.last_name)')
        self.nameInput.setEnabled(False)
        self.nameInput.setText(name[0][0])
        #self.dateEdit.setDate(QDate.currentDate())
        self.choose_all()

        self.submitBtn.clicked.connect(self.assign)
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.chemBtn.clicked.connect(lambda: self.choose("Chemical"))
        self.matBtm.clicked.connect(lambda: self.choose("Material"))
        self.equipBtn.clicked.connect(lambda: self.choose("Equipment"))
        self.pushButton_4.clicked.connect(self.choose_all)

    def choose(self, which):
        data = self.inv.choose_category(which)
        self.comboBox.clear()
        for item_id, name, type, _, _,_ in data:
            self.comboBox.addItem(name + " ("+ type + ")", item_id)

    def choose_all(self):
        data = self.inv.select_inventory_assigntech()
        self.comboBox.clear()
        for item_id, name, type in data:
            self.comboBox.addItem(name + " ("+ type + ")", item_id)

    def assign(self):
        item_id = self.comboBox.currentData()
        quantity = self.quantityInput.text()
        if quantity == "":
            self.notif( "Field cannot be null!",QMessageBox.Icon.Warning) 
        else:
            val = self.tech.assign_item(self.tech_id, item_id, quantity)
            self.notif( val ,QMessageBox.Icon.Information) 
            self.close()
            #print(self.comboBox.currentData(), self.comboBox.currentText())

    def notif(self, message, icon):
        noInput = QMessageBox()
        noInput.setIcon(icon)
        noInput.setText(message)
        noInput.exec()

