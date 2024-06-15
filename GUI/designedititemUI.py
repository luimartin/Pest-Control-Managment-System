from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(608, 474)
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(350, 420, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.label_16 = QtWidgets.QLabel(parent=Dialog)
        self.label_16.setGeometry(QtCore.QRect(20, 0, 271, 81))
        self.label_16.setLineWidth(0)
        self.label_16.setScaledContents(False)
        self.label_16.setIndent(3)
        self.label_16.setObjectName("label_16")
        self.confirmBtn = QtWidgets.QPushButton(parent=Dialog)
        self.confirmBtn.setGeometry(QtCore.QRect(470, 420, 75, 24))
        self.confirmBtn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.confirmBtn.setAutoDefault(True)
        self.confirmBtn.setDefault(False)
        self.confirmBtn.setObjectName("confirmBtn")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(41, 80, 521, 321))
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
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.descInput = QtWidgets.QTextEdit(parent=self.widget)
        self.descInput.setObjectName("descInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descInput)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt;\">Edit Item Information</span></p></body></html>"))
        self.confirmBtn.setText(_translate("Dialog", "Confrim"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Name</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Type</p></body></html>"))
        self.typeInput.setItemText(0, _translate("Dialog", "Chemical"))
        self.typeInput.setItemText(1, _translate("Dialog", "Material"))
        self.typeInput.setItemText(2, _translate("Dialog", "Equipment"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Quantity</p></body></html>"))
        self.dateLabel.setText(_translate("Dialog", "Expiration Date"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Description</p></body></html>"))

from PyQt6.QtWidgets import QDialog,QMessageBox
from PyQt6.QtCore import QDate 
from datetime import date
from inventory import Inventory
class Edititem(QDialog, Ui_Dialog):
    def __init__(self, id, item_type):
        super().__init__()
        self.setupUi(self)
        
        self.i = Inventory()
        self.typeInput.setCurrentText(item_type)
        self.id = id
        
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.typeInput.currentTextChanged.connect(self.on_combo_box_changed)
        self.on_combo_box_changed(item_type)
        placeholder = self.i.select_specific_item(self.id)
        self.nameInput.setText(placeholder[0][0])
        self.quantityInput.setText(str(placeholder[0][1]))
        self.dateEdit.setDate(QDate.fromString(str(placeholder[0][2]), "yyyy-MM-dd"))
        self.descInput.setText(placeholder[0][3])
        #push button function
        self.confirmBtn.clicked.connect(self.editinv)
        
        
    def on_combo_box_changed(self,item_type):
        if item_type == "Chemical":
            
            
            self.dateLabel.setVisible(True)
            self.dateEdit.setVisible(True)
        else:  
            self.dateLabel.setVisible(False)
            self.dateEdit.setVisible(False)

    def editinv(self):
            name = self.nameInput.text()
            self.i.edit_inv_info(self.id, 'item_name', name)
            
            item_type = self.typeInput.currentText()
            self.i.edit_inv_info(self.id, 'item_type', item_type)

            quantity =self.quantityInput.text()
            self.i.edit_inv_info(self.id, 'quantity', quantity)

            if type == "Chemical":
                date = self.dateEdit.date()
                date = date.toString("yyyy-MM-dd")
                self.i.edit_inv_info(self.id, 'expiration', date)
            
            description = self.descInput.toPlainText()
            self.i.edit_inv_info(self.id, 'description', description)
            self.notif("Item Edited")

    def notif(self, name):
        noInput = QMessageBox()
        noInput.setIcon(QMessageBox.Icon.Information)
        noInput.setText("{} Changed".format(name))
        noInput.exec()

