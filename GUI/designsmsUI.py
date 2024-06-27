from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(374, 575)
        self.label_16 = QtWidgets.QLabel(parent=Dialog)
        self.label_16.setGeometry(QtCore.QRect(20, 10, 251, 81))
        self.label_16.setLineWidth(0)
        self.label_16.setScaledContents(False)
        self.label_16.setIndent(3)
        self.label_16.setObjectName("label_16")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(160, 530, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.submitBtn = QtWidgets.QPushButton(parent=Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(260, 530, 75, 24))
        self.submitBtn.setObjectName("submitBtn")
        self.responseText = QtWidgets.QTextEdit(parent=Dialog)
        self.responseText.setEnabled(False)
        self.responseText.setGeometry(QtCore.QRect(30, 410, 319, 91))
        self.responseText.setObjectName("responseText")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 100, 321, 301))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(17)
        self.gridLayout.setObjectName("gridLayout")
        self.msgID = QtWidgets.QComboBox(parent=self.widget)
        self.msgID.setObjectName("msgID")
        self.gridLayout.addWidget(self.msgID, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.typeinput = QtWidgets.QComboBox(parent=self.widget)
        self.typeinput.setObjectName("typeinput")
        self.typeinput.addItem("")
        self.typeinput.addItem("")
        self.gridLayout.addWidget(self.typeinput, 0, 1, 1, 1)
        self.msg = QtWidgets.QTextBrowser(parent=self.widget)
        self.msg.setObjectName("msg")
        self.gridLayout.addWidget(self.msg, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.schedID = QtWidgets.QComboBox(parent=self.widget)
        self.schedID.setObjectName("schedID")
        self.gridLayout.addWidget(self.schedID, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt;\">SMS</span></p></body></html>"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.submitBtn.setText(_translate("Dialog", "Send"))
        self.label.setText(_translate("Dialog", "Schedule ID: "))
        self.typeinput.setItemText(0, _translate("Dialog", "Client"))
        self.typeinput.setItemText(1, _translate("Dialog", "Technician"))
        self.label_2.setText(_translate("Dialog", "Message ID:"))
        self.label_3.setText(_translate("Dialog", "Type: "))


from PyQt6.QtWidgets import QDialog,QMessageBox,QApplication,QHeaderView,QPushButton
from schedule import Schedule
from message import Message
from user import User
class SMS(QDialog,Ui_Dialog):
    def __init__(self, admin):
        super().__init__()
        self.setupUi(self)
        self.message = Message()
        self.sched = Schedule()
        self.u = User()
        self.admin = admin
        idmsg = self.message.show_all()
        sched_id = self.sched.smsview()
        
        for id, name in sched_id:
            self.schedID.addItem('('+ str(id) +') '+name, id)

        for message_id, message_category, message, title in idmsg:
            self.msgID.addItem('('+ str(message_id) +') '+title, message_id)
        self.combo_change()
        self.submitBtn.clicked.connect(self.submit)
        self.msgID.currentIndexChanged.connect(self.combo_change)
        self.cancelBtn.clicked.connect(lambda: self.close())
        
    def submit(self):
        sched_id = self.schedID.currentData()
        msg_contect = self.msg.toPlainText()
        print(self.message.convert_msg(sched_id, msg_contect))
        self.close()
    
    def combo_change(self):
        self.msg.setText(self.message.get_data(self.msgID.currentData(), 'message')[0][0]) 


