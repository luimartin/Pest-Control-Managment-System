from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designassigntechUI import Ui_dialog
from schedule import Schedule
from technician import Technician
from user import User
class AssignTech(QDialog, Ui_dialog):
    def __init__(self, admin, which, sid):
        super().__init__()
        self.setupUi(self)
        self.sched = Schedule()
        self.which = which
        self.sid = sid
        self.u = User()
        self.admin = admin
        techs = self.sched.show_tech()
        self.technicians = Technician()
        self.confirBtn.clicked.connect(self.assign)
        #print(techs)
        self.techbox.clear()  # Clear the combobox before adding new items
        for tech_id, tech_name in techs:
            self.techbox.addItem('('+ str(tech_id) +') '+ tech_name, tech_id)  # Add the tech name as the display text, and the tech_id as the data
            self.techbox.addItem('('+ str(tech_id) +') '+ tech_name, tech_id)  # Add the tech name as the display text, and the tech_id as the data
        self.techbox.setCurrentIndex(0)
        self.cancelBtn.clicked.connect(lambda: self.close())

        sched_id = self.sched.assigntechview()
        
        for id, name in sched_id:
            self.techbox_2.addItem('('+ str(id) +') '+name, id)

        if which == "Edit":

            sched_id = self.sched.smsview()
            self.techbox_2.clear()
            for id, name in sched_id:
                self.techbox_2.addItem('('+ str(id) +') '+name, id)
            
            for i in range(self.techbox_2.count()):
                if self.techbox_2.itemData(i) == sid:
                    self.techbox_2.setCurrentIndex(i)
                    break
            self.techbox.addItem("Remove Assigned Tech", None)
            self.techbox_2.setEnabled(False)

    def assign(self):
    
        tech_id = self.techbox.currentData()
        if self.which == "Edit":
            if self.techbox.currentData() is None:
                # Remove the assigned technician from the specific schedule
                tech = self.sched.get_data(self.sid, 'technician_id')
                print(tech)
                print(tech_id)
                print(f"Removing technician from schedule ID: {self.sid}")  # Debug statement
                self.sched.edit_schedule_info(self.sid, 'technician_id', None)
                #self.technicians.edit_technician_info(tech, 'state', 'Idle')
                self.notif(QMessageBox.Icon.Information, "Remove Assigned Technician")
                self.u.add_backlogs(self.admin, "Remove Assigned Technician")
                
            else:
                if self.sched.assign_technician(self.techbox_2.currentData(), tech_id) == "Technician has a scheduling conflict on the same day.":
                    self.notif(QMessageBox.Icon.Warning, "Technician Unavailable")
                    self.close()
                else:
                    print(f"Editing technician assignment for schedule ID: {self.sid}")  # Debug statement
                    self.u.add_backlogs(self.admin, "Edit Assigned Technician")
                    self.notif(QMessageBox.Icon.Information, "Edit Assigned Technician")

        else:
            if self.technicians.isTechnicianAvailable(tech_id):
                if self.sched.assign_technician(self.techbox_2.currentData(), tech_id) == "Technician has a scheduling conflict on the same day.":
                    self.notif(QMessageBox.Icon.Warning, "Technician Unavailable")
                    self.close()
                else:
                    print(f"Assigning technician to schedule ID: {self.sid}")  # Debug statement
                    self.u.add_backlogs(self.admin, "Assigned Technician")
                    self.notif(QMessageBox.Icon.Information, "Assigned Technician")
                    self.close()
            else:
                self.notif(QMessageBox.Icon.Warning, "Technician Unavailable")

    def notif(self, icon, msg):
        noInput = QMessageBox()
        noInput.setWindowTitle("Notification")
        noInput.setIcon(icon)
        noInput.setText(msg)
        noInput.exec()
        
"""app = QApplication([])
window = AssignTech("HF00010", "Edit", 28)
window.show()
app.exec()"""

