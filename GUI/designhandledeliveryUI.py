from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 577)
        Dialog.setStyleSheet("background-color: white;")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 431, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.typeInput = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.typeInput.setObjectName("typeInput")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.typeInput.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.typeInput)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.quantityInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.quantityInput.setObjectName("quantityInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.quantityInput)
        self.dateLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dateLabel)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.descInput = QtWidgets.QTextEdit(parent=self.layoutWidget)
        self.descInput.setObjectName("descInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descInput)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.supplierInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supplierInput.setObjectName("supplierInput")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.supplierInput)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.deliveryInput = QtWidgets.QDateTimeEdit(parent=self.layoutWidget)
        self.deliveryInput.setObjectName("deliveryInput")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.deliveryInput)
        self.comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        self.addBtn = QtWidgets.QPushButton(parent=Dialog)
        self.addBtn.setGeometry(QtCore.QRect(365, 520, 75, 24))
        self.addBtn.setObjectName("addBtn")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(250, 520, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Add Delivery</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Name</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Type"))
        self.typeInput.setItemText(0, _translate("Dialog", "Chemical"))
        self.typeInput.setItemText(1, _translate("Dialog", "Material"))
        self.typeInput.setItemText(2, _translate("Dialog", "Equipment"))
        self.label_3.setText(_translate("Dialog", "Quantity"))
        self.dateLabel.setText(_translate("Dialog", "Expiration Date"))
        self.label_5.setText(_translate("Dialog", "Description"))
        self.label_4.setText(_translate("Dialog", "Supplier Name:"))
        self.label_6.setText(_translate("Dialog", "Delivery Date"))
        self.addBtn.setText(_translate("Dialog", "Update"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
# if eedit remove the runner dito
from PyQt6.QtWidgets import QDialog,QMessageBox
from inventory import Inventory
from user import User
class HandleDelivery(QDialog, Ui_Dialog):
    def __init__(self, admin):
        super().__init__()
        self.setupUi(self)
        self.i = Inventory()
        self.u = User()
        self.admin = admin
        data = self.i.select_inventory()
        self.typeInput.setEnabled(False)
        self.descInput.setEnabled(False)
        self.deliveryInput.setDateTime(QtCore.QDateTime.currentDateTime())
        #####ibahin to if needed
        self.deliveryInput.setEnabled(False)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        # Populate the QComboBox
        for item_id, item_name, _, _, _, _, _, _ in data:
            self.comboBox.addItem(item_name, item_id)

        # Set the initial placeholder text
        self.set_placeholder_text(self.comboBox.currentData())
        self.on_type_changed(self.typeInput.currentText())
        # Connect the currentIndexChanged signal to update the placeholder text
        self.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)
        self.typeInput.currentTextChanged.connect(self.on_type_changed)
        self.addBtn.clicked.connect(self.update)
        self.cancelBtn.clicked.connect(lambda: self.close())

    def set_placeholder_text(self, item_id):
        placeholder = self.i.select_specific_item(item_id)
        self.descInput.setPlaceholderText(placeholder[0][3])
        self.supplierInput.setText(placeholder[0][5])
        self.typeInput.setCurrentText(placeholder[0][4])

    def on_combo_box_changed(self, index):
        selected_item_id = self.comboBox.itemData(index)
        self.set_placeholder_text(selected_item_id)
        self.on_type_changed(self.typeInput.currentText())

    def on_type_changed(self, item_type):
        if item_type == "Chemical":
            self.dateLabel.setVisible(True)
            self.dateEdit.setVisible(True)
        else:
            self.dateLabel.setVisible(False)
            self.dateEdit.setVisible(False)
    
    def update(self):
        quantity = self.quantityInput.text()
        exp = self.dateEdit.date()
        exp = exp.toString("yyyy-MM-dd")
        deliver = self.deliveryInput.dateTime()
        deliver = deliver.toString("yyyy-MM-dd HH:mm:ss")
        if quantity == "":
            self.notif("Input Inadequate", QMessageBox.Icon.Warning)
        else:    
            if self.typeInput.currentText() == "Chemical":
                self.i.stock_item(self.comboBox.currentData(), quantity
                ,exp, self.supplierInput.text(), deliver)
        
            else:
                self.i.stock_item(self.comboBox.currentData(), quantity
                ,None, self.supplierInput.text(), deliver)
            self.u.add_backlogs(self.admin, "Delivey Added")
            self.notif("Item Updated", QMessageBox.Icon.Information)

    def notif(self, message, icon):
        noInput = QMessageBox()
        noInput.setIcon(icon)
        noInput.setText(message)
        noInput.exec()