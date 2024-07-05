from PyQt6.QtWidgets import QDialog,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton,QApplication
from PyQt6.QtCore import QDate
from PyQt6 import QtGui, QtCore
from GUI.designaddcontractUI import Ui_Dialog
from datetime import date
from contract import Contract
from user import User
class AddContract(QDialog,Ui_Dialog):
    def __init__(self, client_id, cont_id, which, admin):
        super().__init__()
        self.id = client_id
        self.cont_id = cont_id
        self.which = which
        self.setupUi(self)
        self.c = Contract()
        self.u = User()
        self.admin = admin
        self.addBtn.clicked.connect(self.addcontract)
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.lineEdit_3.setValidator(QtGui.QDoubleValidator(0.0, 5.0, 4))
        self.scopeInput.setValidator(QtGui.QDoubleValidator(0.0, 5.0, 4))
        self.unitInput.setValidator(QtGui.QIntValidator())
        if self.which == "Edit":
            self.label_17.setText(QtCore.QCoreApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt;\">Edit Contract</span></p></body></html>"))
            placeholder = self.c.contract_view(self.id)
            self.problemInput.setText(placeholder[0][0])
            self.typeInput.setText(placeholder[0][1])
            self.startInput.setDate(QDate.fromString(str(placeholder[0][2]), "yyyy-MM-dd")) 
            self.endInput.setDate(QDate.fromString(str(placeholder[0][3]), "yyyy-MM-dd"))
            self.scopeInput.setText(str(placeholder[0][4]))
            self.unitInput.setText(str(placeholder[0][5]))
            self.lineEdit_3.setText(str(placeholder[0][6]))
        else: 
            self.endInput.setDate(date.today())
            self.startInput.setDate(date.today())
    def addcontract(self):
        if self.which == "Add":
            problem = self.problemInput.text()
            treatment = self.typeInput.text()
            start = self.startInput.date()
            start = start.toString("yyyy-MM-dd")
            end = self.endInput.date()
            end = end.toString("yyyy-MM-dd")  
            scope =self.scopeInput.text()
            unit = self.unitInput.text()
            price = self.lineEdit_3.text()  

            if (problem and treatment and start and end and scope and unit and price) == "":
                self.notif(QMessageBox.Icon.Warning, "Field cannot be null")
            elif start == end:
                self.notif(QMessageBox.Icon.Warning, "Start and End Dates cannot be the same")
            elif start >= end:
                self.notif(QMessageBox.Icon.Warning, "Start Date cannot be greater than End Date")  
            else:
                self.c.add_contract(self.id, problem, treatment, start, end, scope, unit, price)
                self.u.add_backlogs(self.admin, "Added Contract")
                self.notif(QMessageBox.Icon.Information, "Contract Added")  

        else:
            treatment = self.typeInput.text()
            end = self.endInput.date()
            end = end.toString("yyyy-MM-dd")
            start = self.startInput.date()
            start = start.toString("yyyy-MM-dd")
            scope =self.scopeInput.text()
            unit = self.unitInput.text()
            price = self.lineEdit_3.text()  
            problem = self.problemInput.text()
            if (problem and treatment and start and end and scope and unit and price) == "":
                self.notif(QMessageBox.Icon.Warning, "Field cannot be null")
            elif start == end:
                self.notif(QMessageBox.Icon.Warning, "Start and End Dates cannot be the same")
            elif start >= end:
                self.notif(QMessageBox.Icon.Warning, "Start Date cannot be greater than End Date")  
            else:
                self.c.edit_contract_info(self.cont_id, self.id, "problem", problem)
                self.c.edit_contract_info(self.cont_id, self.id, "service_type", treatment)
                self.c.edit_contract_info(self.cont_id, self.id, "start_date", start)
                self.c.edit_contract_info(self.cont_id, self.id, "end_date", end)
                self.c.edit_contract_info(self.cont_id, self.id, "square_meter", scope)
                self.c.edit_contract_info(self.cont_id, self.id, "unit", unit)
                self.c.edit_contract_info(self.cont_id, self.id, "price", price)
                self.u.add_backlogs(self.admin, "Edited Contract")
                self.notif(QMessageBox.Icon.Information, "Contract Edited")

    def notif(self, icon, msg):
        noInput = QMessageBox()
        noInput.setWindowTitle("Notificaiton")
        noInput.setIcon(icon)
        noInput.setText(msg)
        noInput.exec()