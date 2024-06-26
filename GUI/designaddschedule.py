from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(602, 315)
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(320, 270, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.confirmBtn = QtWidgets.QPushButton(parent=Dialog)
        self.confirmBtn.setGeometry(QtCore.QRect(450, 270, 75, 24))
        self.confirmBtn.setObjectName("confirmBtn")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(31, 40, 541, 231))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.defaultinfo = QtWidgets.QWidget(parent=self.widget)
        self.defaultinfo.setObjectName("defaultinfo")
        self.layoutWidget = QtWidgets.QWidget(parent=self.defaultinfo)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 531, 116))
        self.layoutWidget.setObjectName("layoutWidget")
        self._2 = QtWidgets.QGridLayout(self.layoutWidget)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setObjectName("_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.dayinput = QtWidgets.QDateEdit(parent=self.layoutWidget)
        self.dayinput.setObjectName("dayinput")
        self.horizontalLayout_3.addWidget(self.dayinput)
        self._2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.timeinInput = QtWidgets.QTimeEdit(parent=self.layoutWidget)
        self.timeinInput.setObjectName("timeinInput")
        self.horizontalLayout_4.addWidget(self.timeinInput)
        self.label_10 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.timeoutInput = QtWidgets.QTimeEdit(parent=self.layoutWidget)
        self.timeoutInput.setObjectName("timeoutInput")
        self.horizontalLayout_4.addWidget(self.timeoutInput)
        self._2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.defaultinfo, 3, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.postinginfo = QtWidgets.QWidget(parent=self.widget)
        self.postinginfo.setObjectName("postinginfo")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.postinginfo)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 531, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.startInput = QtWidgets.QDateEdit(parent=self.layoutWidget1)
        self.startInput.setObjectName("startInput")
        self.horizontalLayout.addWidget(self.startInput)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.endInput = QtWidgets.QDateEdit(parent=self.layoutWidget1)
        self.endInput.setObjectName("endInput")
        self.horizontalLayout.addWidget(self.endInput)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.postinginfo, 2, 0, 1, 2)
        self.clientComboBox = QtWidgets.QComboBox(parent=self.widget)
        self.clientComboBox.setObjectName("clientComboBox")
        self.gridLayout_2.addWidget(self.clientComboBox, 0, 1, 1, 1)
        self.layoutWidget.raise_()
        self.cancelBtn.raise_()
        self.confirmBtn.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.confirmBtn.setText(_translate("Dialog", "Confirm"))
        self.label_2.setText(_translate("Dialog", "    Type of Schedule:    "))
        self.label.setText(_translate("Dialog", "    Client ID: "))
        self.label_8.setText(_translate("Dialog", "Day of Treatment:"))
        self.label_9.setText(_translate("Dialog", "Time in and out:"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Start:</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">End:</p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "Posting"))
        self.comboBox.setItemText(1, _translate("Dialog", "Default"))
        self.label_3.setText(_translate("Dialog", "Date of Treatment:"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Start:</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">End:</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Time in and out:"))
        self.label_7.setText(_translate("Dialog", "9:00AM - 5:00PM"))

from PyQt6.QtWidgets import QDialog,QMessageBox, QApplication
from PyQt6.QtCore import QTime 
from datetime import date
from clientinfo import ClientInfo
from schedule import Schedule
from user import User
# if edit tangalin yung runner dito
class AddSchedule(QDialog, Ui_Dialog):
    def __init__(self, which, sched_id, admin):
        super().__init__()
        self.setupUi(self)
        self.on_combo_box_changed(0)
        self.sched_id = sched_id
        self.which = which
        self.u = User()
        self.admin = admin

        self.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.confirmBtn.clicked.connect(self.add)
        self.c = ClientInfo()
        self.s = Schedule()
        
        self.startInput.setDate(date.today())
        self.endInput.setDate(date.today())
        self.dayinput.setDate(date.today())
        self.timeinInput.setTime(QTime.currentTime())
        self.timeoutInput.setTime(QTime.currentTime())
        clients = self.c.select_all_clients()
        self.clientComboBox.clear()

        for client_id, name, phone_num, status in clients:
            self.clientComboBox.addItem(f"{name}", client_id)

        if which == "Edit":
            placeholder = self.s.placeholder_sched(sched_id)
            self.clientComboBox.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.clientComboBox.setCurrentText(placeholder[0][0])
            self.comboBox.setCurrentText(placeholder[0][1])
            self.startInput.setDate(QtCore.QDate.fromString(str(placeholder[0][2]), "yyyy-MM-dd"))
            self.endInput.setDate(QtCore.QDate.fromString(str(placeholder[0][3]), "yyyy-MM-dd"))
            self.dayinput.setDate(QtCore.QDate.fromString(str(placeholder[0][2]), "yyyy-MM-dd"))
            self.timeinInput.setTime(QtCore.QTime.fromString(str(placeholder[0][4]), "HH:mm:ss"))
            self.timeoutInput.setTime(QtCore.QTime.fromString(str(placeholder[0][5]), "HH:mm:ss"))
    def add(self):
        treatment =self.comboBox.currentText()
        id = self.clientComboBox.currentData()
        start_date = self.startInput.date()
        start_date= start_date.toString("yyyy-MM-dd")
        end_date = self.endInput.date()
        day = self.dayinput.date()
        day = day.toString("yyyy-MM-dd")
        time_in = self.timeinInput.time()
        time_in = time_in.toString("HH:mm:ss")
        time_out = self.timeoutInput.time()
        time_out = time_out.toString("HH:mm:ss")
        end_date = end_date.toString("yyyy-MM-dd")
        print(start_date, end_date)
        if self.which == "Edit":
            if treatment == "Posting":
                if start_date == end_date: self.notif(QMessageBox.Icon.Warning, "Start Date and End Date is the Same!")
                elif start_date > end_date: self.notif(QMessageBox.Icon.Warning, "Start Date cannot be greater than End Date")
                else:
                    print(treatment, id, self.sched_id)
                    self.s.posting_modifier(self.sched_id, start_date, end_date)
                    self.u.add_backlogs(self.admin, "Edited Schedule")
                    self.notif(QMessageBox.Icon.Information, "Schedule Edited" )
                    self.close()
            else:
                if start_date == end_date: self.notif(QMessageBox.Icon.Warning, "Start Date and End Date is the Same!")
                elif start_date > end_date: self.notif(QMessageBox.Icon.Warning, "Start Date cannot be greater than End Date")
                else:
                    self.s.edit_schedule_info(self.sched_id, 'start_date', day)
                    self.s.edit_schedule_info(self.sched_id, 'end_date', day)
                    self.s.edit_schedule_info(self.sched_id, 'time_in', time_in)
                    self.s.edit_schedule_info(self.sched_id, 'time_out', time_out)
                    self.u.add_backlogs(self.admin, "Edited Schedule")
                    self.notif(QMessageBox.Icon.Information, "Schedule Edited" )
                    self.close()
        else:
            if treatment == "Posting":

                if start_date == end_date: self.notif(QMessageBox.Icon.Warning, "Start Date and End Date is the Same!")
                elif start_date > end_date: self.notif(QMessageBox.Icon.Warning, "Start Date cannot be greater than End Date")
            
                else: 
                    self.s.add_schedule(id, treatment, start_date, end_date, "09:00:00", "17:00:00")
                    self.notif(QMessageBox.Icon.Information, "Schedule Added" )
                    self.u.add_backlogs(self.admin, "Added Schedule")
                    self.close()
            else:

                if time_in == time_out: self.notif(QMessageBox.Icon.Warning, "Start Time and End Time is the Same!")
                elif time_in > time_out: self.notif(QMessageBox.Icon.Warning, "Time in cannot be greater than Time out")
                else: 
                    self.s.add_schedule(id, treatment, day, day, time_in, time_out)
                    self.notif(QMessageBox.Icon.Information, "Schedule Added" )
                    self.u.add_backlogs(self.admin, "Added Schedule")
                    self.close()
        
    def notif(self, type, message):
        noInput = QMessageBox()
        noInput.setIcon(type)
        noInput.setText(message)
        noInput.exec()

    def on_combo_box_changed(self, index):
        if index == 0:
            self.postinginfo.setVisible(True)
            self.defaultinfo.setVisible(False)
        else:
            self.postinginfo.setVisible(False)
            self.defaultinfo.setVisible(True)