from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(474, 480)
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 391, 71))
        self.label_6.setLineWidth(0)
        self.label_6.setScaledContents(False)
        self.label_6.setIndent(3)
        self.label_6.setObjectName("label_6")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(210, 410, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.addBtn = QtWidgets.QPushButton(parent=Dialog)
        self.addBtn.setGeometry(QtCore.QRect(330, 410, 75, 24))
        self.addBtn.setObjectName("addBtn")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 110, 411, 231))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(24)
        self.gridLayout.setVerticalSpacing(22)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.firstnameInput = QtWidgets.QLineEdit(parent=self.widget)
        self.firstnameInput.setObjectName("firstnameInput")
        self.gridLayout.addWidget(self.firstnameInput, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lastnameInput = QtWidgets.QLineEdit(parent=self.widget)
        self.lastnameInput.setObjectName("lastnameInput")
        self.gridLayout.addWidget(self.lastnameInput, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.phonenoInput = QtWidgets.QLineEdit(parent=self.widget)
        self.phonenoInput.setObjectName("phonenoInput")
        self.gridLayout.addWidget(self.phonenoInput, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.locationInput = QtWidgets.QLineEdit(parent=self.widget)
        self.locationInput.setObjectName("locationInput")
        self.gridLayout.addWidget(self.locationInput, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt;\">Add Technician</span></p><p><br/></p></body></html>"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.addBtn.setText(_translate("Dialog", "Submit"))
        self.label.setText(_translate("Dialog", "First Name: "))
        self.label_2.setText(_translate("Dialog", "Last Name: "))
        self.label_3.setText(_translate("Dialog", "Phone No: "))
        self.label_4.setText(_translate("Dialog", "Location: "))


from PyQt6.QtWidgets import QDialog,QMessageBox, QApplication

from technician import Technician
from user import User
# if edit tangalin yung runner dito
class AddTechnician(QDialog, Ui_Dialog):
    def __init__(self, which, techid, admin):
        super().__init__()
        self.t = Technician()
        self.setupUi(self)
        self.techid = techid
        self.u = User()
        self.admin = admin
        self.addBtn.clicked.connect(self.add)
        self.cancelBtn.clicked.connect(lambda: self.close())
        regex = QtCore.QRegularExpression(r"^0\d{0,10}$")
        validator = QtGui.QRegularExpressionValidator(regex, self)
        self.phonenoInput.setValidator(validator)
        self.which = which
        if which == "Edit":
            self.label_6.setText(QtCore.QCoreApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt;\">Edit Technician</span></p><p><br/></p></body></html>"))
            placeholder = self.t.select_specific_tech(techid)
            self.firstnameInput.setText(placeholder[0][0])
            self.lastnameInput.setText(placeholder[0][1])
            self.phonenoInput.setText(placeholder[0][2])
            self.locationInput.setText(placeholder[0][3])
            print(techid)

    def add(self):
        fname = self.firstnameInput.text()
        lname = self.lastnameInput.text()
        phoneno = self.phonenoInput.text()
        address = self.locationInput.text()
        if self.which == "Edit":
            self.t.edit_technician_info(self.techid, 'first_name', fname)
            self.t.edit_technician_info(self.techid, 'last_name', lname)
            self.t.edit_technician_info(self.techid, 'phone_num', phoneno)
            self.t.edit_technician_info(self.techid, 'address', address)
            self.u.add_backlogs(self.admin, "Technician Edited")
            self.notif(QMessageBox.Icon.Information, "Technician Info Edited")
            self.close()
            
        else:
            if (fname and lname and phoneno and address) == "":
                self.notif(QMessageBox.Icon.Warning, "All Fields cannot be null")
            else: 
                self.t.add_technician(fname, lname, phoneno, address)
                self.notif(QMessageBox.Icon.Information, "Technician Added")
                self.u.add_backlogs(self.admin, "Technician Added")
                print(fname, lname, phoneno, address)
                self.close()

    def notif(self, type, message):
        noInput = QMessageBox()
        noInput.setIcon(type)
        noInput.setText(message)
        noInput.exec()
