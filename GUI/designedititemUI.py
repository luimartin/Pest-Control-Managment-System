from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog,QMessageBox,QApplication
from datetime import date
from inventory import Inventory

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 474)
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(470, 400, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 541, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(1, 1, 5, 0)
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.quantityInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.quantityInput.setObjectName("quantityInput")
        self.gridLayout.addWidget(self.quantityInput, 2, 1, 1, 1)
        self.nameInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.nameInput.setObjectName("nameInput")
        self.gridLayout.addWidget(self.nameInput, 0, 1, 1, 1)
        self.typeBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.typeBtn.setObjectName("typeBtn")
        self.gridLayout.addWidget(self.typeBtn, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.typeInput = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.typeInput.setObjectName("typeInput")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.gridLayout.addWidget(self.typeInput, 1, 1, 1, 1)
        self.quantityBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.quantityBtn.setObjectName("quantityBtn")
        self.gridLayout.addWidget(self.quantityBtn, 2, 2, 1, 1)
        self.dateLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout.addWidget(self.dateLabel, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.nameBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.nameBtn.setObjectName("nameBtn")
        self.gridLayout.addWidget(self.nameBtn, 0, 2, 1, 1)
        self.dateBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.dateBtn.setObjectName("dateBtn")
        self.gridLayout.addWidget(self.dateBtn, 3, 2, 1, 1)
        self.descInput = QtWidgets.QTextEdit(parent=self.layoutWidget)
        self.descInput.setObjectName("descInput")
        self.gridLayout.addWidget(self.descInput, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.descBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.descBtn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.descBtn.setAutoDefault(True)
        self.descBtn.setDefault(False)
        self.descBtn.setObjectName("descBtn")
        self.gridLayout.addWidget(self.descBtn, 5, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Name</p></body></html>"))
        self.typeBtn.setText(_translate("Dialog", "Confrim"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Description</p></body></html>"))
        self.typeInput.setItemText(0, _translate("Dialog", "Chemical"))
        self.typeInput.setItemText(1, _translate("Dialog", "Material"))
        self.typeInput.setItemText(2, _translate("Dialog", "Equipment"))
        self.quantityBtn.setText(_translate("Dialog", "Confrim"))
        self.dateLabel.setText(_translate("Dialog", "Expiration Date"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Type</p></body></html>"))
        self.nameBtn.setText(_translate("Dialog", "Confrim"))
        self.dateBtn.setText(_translate("Dialog", "Confrim"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Quantity</p></body></html>"))
        self.descBtn.setText(_translate("Dialog", "Confrim"))

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
        print(placeholder[0][2])
        self.descInput.setText(placeholder[0][3])
        #push button function
        self.nameBtn.clicked.connect(lambda: self.editinv(1))
        self.typeBtn.clicked.connect(lambda: self.editinv(2))
        self.quantityBtn.clicked.connect(lambda: self.editinv(3))
        self.dateBtn.clicked.connect(lambda: self.editinv(4))
        self.descBtn.clicked.connect(lambda: self.editinv(5))
        
        
    def on_combo_box_changed(self,item_type):
        if item_type == "Chemical":
            today = date.today()
            self.dateEdit.setDate(today)
            self.dateLabel.setVisible(True)
            self.dateEdit.setVisible(True)
            self.dateBtn.setVisible(True)
        else:  
            self.dateBtn.setVisible(False)
            self.dateLabel.setVisible(False)
            self.dateEdit.setVisible(False)

    def editinv(self, categ):
        if categ == 1:
            name = self.nameInput.text()
            self.i.edit_inv_info(self.id, 'item_name', name)
            self.notif("Name")
        elif categ == 2:
            item_type = self.typeInput.currentText()
            self.i.edit_inv_info(self.id, 'item_type', item_type)
            self.notif("Type")
        elif categ == 3:
            quantity =self.quantityInput.text()
            self.i.edit_inv_info(self.id, 'quantity', quantity)
            self.notif("Quantity")
        elif categ == 4:
            date = self.dateEdit.date()
            date = date.toString("yyyy-MM-dd")
            self.i.edit_inv_info(self.id, 'expiration', date)
            self.notif("Expiration Date")
        else:
            description = self.descInput.toPlainText()
            self.i.edit_inv_info(self.id, 'description', description)
            self.notif("Description")

    def notif(self, name):
        noInput = QMessageBox()
        noInput.setIcon(QMessageBox.Icon.Information)
        noInput.setText("{} Changed".format(name))
        noInput.exec()

