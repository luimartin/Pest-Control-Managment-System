from PyQt6.QtWidgets import QDialog,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton,QApplication
from PyQt6.QtCore import QDate 
from GUI.designaddcontractUI import Ui_addcontract
from datetime import date
from contract import Contract
from user import User
class AddContract(QDialog,Ui_addcontract):
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

        if self.which == "Edit":
            placeholder = self.c.contract_view(self.id)
            self.problemInput.setText(placeholder[0][0])
            self.typeInput.setText(placeholder[0][1])
            self.startInput.setDate(QDate.fromString(str(placeholder[0][2]), "yyyy-MM-dd")) 
            self.endInput.setDate(QDate.fromString(str(placeholder[0][3]), "yyyy-MM-dd"))
            self.scopeInput.setText(str(placeholder[0][4]))
            self.unitInput.setText(str(placeholder[0][5]))
            self.priceInput.setText(str(placeholder[0][6]))
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
            price = self.priceInput.text()  
            self.c.add_contract(self.id, problem, treatment, start, end, scope, unit, price)
            self.u.add_backlogs(self.admin, "Added Contract")
            noInput = QMessageBox()
            noInput.setWindowTitle("Notificaiton")
            noInput.setIcon(QMessageBox.Icon.Information)
            noInput.setText("Contract Added")
            noInput.exec()
            self.close()
        else:
            # get data
            problem = self.problemInput.text()
            self.c.edit_contract_info(self.cont_id, self.id, "problem", problem)

            treatment = self.typeInput.text()
            self.c.edit_contract_info(self.cont_id, self.id, "service_type", treatment)

            start = self.startInput.date()
            start = start.toString("yyyy-MM-dd")
            self.c.edit_contract_info(self.cont_id, self.id, "start_date", start)

            end = self.endInput.date()
            end = end.toString("yyyy-MM-dd")
            self.c.edit_contract_info(self.cont_id, self.id, "end_date", end)

            scope =self.scopeInput.text()
            self.c.edit_contract_info(self.cont_id, self.id, "square_meter", scope)

            unit = self.unitInput.text()
            self.c.edit_contract_info(self.cont_id, self.id, "unit", unit)

            price = self.priceInput.text()  
            self.c.edit_contract_info(self.cont_id, self.id, "price", price)

            self.u.add_backlogs(self.admin, "Edited Contract")
            noInput = QMessageBox()
            noInput.setWindowTitle("Notificaiton")
            noInput.setIcon(QMessageBox.Icon.Information)
            noInput.setText("Contract Edited")
            noInput.exec()
            self.close()
