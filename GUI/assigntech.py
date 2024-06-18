from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designassigntechUI import Ui_dialog
from schedule import Schedule
from technician import Technician
class AssignTech(QDialog, Ui_dialog):
    def __init__(self, sched_id):
        super().__init__()
        self.setupUi(self)
        self.sched_id = sched_id
        self.sched = Schedule()
        techs = self.sched.show_tech()

        self.technicians = Technician()


        self.confirBtn.clicked.connect(self.assign)
        #print(techs)
        self.techbox.clear()  # Clear the combobox before adding new items
        for tech_id, tech_name in techs:
            self.techbox.addItem(tech_name, tech_id)  # Add the tech name as the display text, and the tech_id as the data
        self.techbox.setCurrentIndex(0)
        self.cancelBtn.clicked.connect(lambda: self.close())
    def assign(self):
        tech_id = self.techbox.currentData()
        if self.technicians.isTechnicianAvailable(tech_id):
            
            self.sched.assign_technician(self.sched_id, tech_id)
            noInput = QMessageBox()
            noInput.setWindowTitle("Notification")
            noInput.setIcon(QMessageBox.Icon.Information)
            noInput.setText("Assign Technician")
            noInput.exec()
            self.close()

        else:
            noInput = QMessageBox()
            noInput.setWindowTitle("Notification")
            noInput.setIcon(QMessageBox.Icon.Warning)
            noInput.setText("Technician Unavailable")
            noInput.exec()


