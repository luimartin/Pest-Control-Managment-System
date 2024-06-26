from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 443)
        self.label_16 = QtWidgets.QLabel(parent=Dialog)
        self.label_16.setGeometry(QtCore.QRect(20, 10, 251, 81))
        self.label_16.setLineWidth(0)
        self.label_16.setScaledContents(False)
        self.label_16.setIndent(3)
        self.label_16.setObjectName("label_16")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(21, 101, 68, 16))
        self.label.setObjectName("label")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(150, 390, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.submitBtn = QtWidgets.QPushButton(parent=Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(250, 390, 75, 24))
        self.submitBtn.setObjectName("submitBtn")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(21, 101, 331, 271))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(23)
        self.formLayout.setObjectName("formLayout")
        self.schedID = QtWidgets.QComboBox(parent=self.widget)
        self.schedID.setObjectName("schedID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.schedID)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.msgID = QtWidgets.QComboBox(parent=self.widget)
        self.msgID.setObjectName("msgID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.msgID)
        self.msg = QtWidgets.QTextBrowser(parent=self.widget)
        self.msg.setObjectName("msg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.msg)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt;\">SMS</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Schedule ID: "))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.submitBtn.setText(_translate("Dialog", "Submit"))
        self.label_2.setText(_translate("Dialog", "Message ID:"))

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


