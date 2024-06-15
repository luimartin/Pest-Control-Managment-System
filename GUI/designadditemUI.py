
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog,QMessageBox
from inventory import Inventory
from datetime import date
# if edit tangalin yung runner dito
class Ui_addItem(object):
    def setupUi(self, addItem):
        addItem.setObjectName("addItem")
        addItem.resize(464, 466)
        addItem.setMouseTracking(False)
        #addItem.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        addItem.setSizeGripEnabled(False)
        addItem.setModal(False)
        self.addBtn = QtWidgets.QPushButton(parent=addItem)
        self.addBtn.setGeometry(QtCore.QRect(320, 400, 75, 24))
        self.addBtn.setObjectName("addBtn")
        self.cancelBtn = QtWidgets.QPushButton(parent=addItem)
        self.cancelBtn.setGeometry(QtCore.QRect(205, 403, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.widget = QtWidgets.QWidget(parent=addItem)
        self.widget.setGeometry(QtCore.QRect(10, 50, 441, 311))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.nameInput = QtWidgets.QLineEdit(parent=self.widget)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameInput)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.typeInput = QtWidgets.QComboBox(parent=self.widget)
        self.typeInput.setObjectName("typeInput")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.typeInput)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.quantityInput = QtWidgets.QLineEdit(parent=self.widget)
        self.quantityInput.setObjectName("quantityInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.quantityInput)
        self.dateLabel = QtWidgets.QLabel(parent=self.widget)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dateLabel)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.descInput = QtWidgets.QTextEdit(parent=self.widget)
        self.descInput.setObjectName("descInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descInput)

        self.retranslateUi(addItem)
        QtCore.QMetaObject.connectSlotsByName(addItem)

    def retranslateUi(self, addItem):
        _translate = QtCore.QCoreApplication.translate
        addItem.setWindowTitle(_translate("addItem", "Dialog"))
        self.addBtn.setText(_translate("addItem", "Add"))
        self.cancelBtn.setText(_translate("addItem", "Cancel"))
        self.label.setText(_translate("addItem", "<html><head/><body><p align=\"center\">Name</p></body></html>"))
        self.label_2.setText(_translate("addItem", "Type"))
        self.typeInput.setItemText(0, _translate("addItem", "Chemical"))
        self.typeInput.setItemText(1, _translate("addItem", "Material"))
        self.typeInput.setItemText(2, _translate("addItem", "Equipment"))
        self.label_3.setText(_translate("addItem", "Quantity"))
        self.dateLabel.setText(_translate("addItem", "Expiration Date"))
        self.label_5.setText(_translate("addItem", "Description"))


class AddItem(QDialog, Ui_addItem):
    def __init__(self, index):
        super().__init__()
        self.setupUi(self)
        today = date.today()
        self.dateEdit.setDate(today)
        self.typeInput.setCurrentIndex(index)
        self.on_combo_box_changed(index)
        self.typeInput.currentIndexChanged.connect(self.on_combo_box_changed)
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.addBtn.clicked.connect(self.add)
        self.i = Inventory()

    def add(self):
        name = self.nameInput.text()
        date = self.dateEdit.date()
        date = date.toString("yyyy-MM-dd")
        quantity =self.quantityInput.text()
        description = self.descInput.toPlainText()
        type = self.typeInput.currentText()
        
        if (name and quantity) != "":
            if type == "Chemical":
                self.i.add_item(name, type, quantity, description, date)
            else:
                self.i.add_item(name, type, quantity, description, None)
            
            noInput = QMessageBox()
            noInput.setIcon(QMessageBox.Icon.Information)
            noInput.setText("Item Added")
            noInput.exec()
            self.close()
        else:
            noInput = QMessageBox()
            noInput.setIcon(QMessageBox.Icon.Warning)
            noInput.setText("Input Name and Quantity Textfield")
            noInput.exec()


    def on_combo_box_changed(self,index):
        if index == 0:

            self.dateLabel.setVisible(True)
            self.dateEdit.setVisible(True)
        
        else:  

            self.dateLabel.setVisible(False)
            self.dateEdit.setVisible(False)