from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 568)
        self.submitBtn = QtWidgets.QPushButton(parent=Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(380, 520, 75, 24))
        self.submitBtn.setObjectName("submitBtn")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(270, 520, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 391, 71))
        self.label_9.setLineWidth(0)
        self.label_9.setScaledContents(False)
        self.label_9.setIndent(3)
        self.label_9.setObjectName("label_9")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 100, 421, 381))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(18)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.userInput = QtWidgets.QLineEdit(parent=self.widget)
        self.userInput.setObjectName("userInput")
        self.gridLayout.addWidget(self.userInput, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.passInput = QtWidgets.QLineEdit(parent=self.widget)
        self.passInput.setObjectName("passInput")
        self.gridLayout.addWidget(self.passInput, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.q1Input = QtWidgets.QComboBox(parent=self.widget)
        self.q1Input.setObjectName("q1Input")
        self.gridLayout.addWidget(self.q1Input, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.ans1Input = QtWidgets.QLineEdit(parent=self.widget)
        self.ans1Input.setObjectName("ans1Input")
        self.gridLayout.addWidget(self.ans1Input, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.q2Input = QtWidgets.QComboBox(parent=self.widget)
        self.q2Input.setObjectName("q2Input")
        self.gridLayout.addWidget(self.q2Input, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.ans2Input = QtWidgets.QLineEdit(parent=self.widget)
        self.ans2Input.setObjectName("ans2Input")
        self.gridLayout.addWidget(self.ans2Input, 6, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.submitBtn.setText(_translate("Dialog", "Submit"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt;\">Add Admin</span></p><p><br/></p></body></html>"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Confirm </p><p>Password</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "Question 1"))
        self.label_6.setText(_translate("Dialog", "Answer 1"))
        self.label_7.setText(_translate("Dialog", "Question 2"))
        self.label_8.setText(_translate("Dialog", "Answer 2"))

from PyQt6.QtWidgets import QDialog,QMessageBox, QApplication
from user import User

# if edit tangalin yung runner dito
class AddAdmin(QDialog, Ui_Dialog):
    def __init__(self, admin):
        super().__init__()
        self.setupUi(self)
        self.passInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.user = User()
        self.admin = admin
        self.cancelBtn.clicked.connect(lambda: self.close())
        for sec in self.user.security_question:
            self.q1Input.addItem(sec)
            self.q2Input.addItem(sec)
        self.q2Input.setCurrentIndex(1)
        self.submitBtn.clicked.connect(self.addadmin)
    def addadmin(self):
        user = self.userInput.text()
        password = self.passInput.text()
        confirmpass = self.lineEdit_3.text()
        q1 = self.q1Input.currentText()
        q2 = self.q2Input.currentText()
        a1 = self.ans1Input.text()
        a2 = self.ans2Input.text()

        if (user and password and confirmpass and q1 and q2 and a1 and a2) == "":
            self.notif("Fields cannot be null!", QMessageBox.Icon.Warning)
        elif password != confirmpass:
            self.notif("Password does not match", QMessageBox.Icon.Warning)
        elif q1 == q2:
            self.notif("Questions cannot be the same!", QMessageBox.Icon.Warning)
        else:
            self.user.add_user(user, password, q1, a1, q2, a2)
            self.user.add_backlogs(self.admin, "Admin Added")
            self.notif("Admin Added", QMessageBox.Icon.Information)
            self.close()
        print(user, password, confirmpass, q1, q2, a1, a2)
    
    def notif(self, message, icon):
        #QMessageBox.Icon.Information
        noInput = QMessageBox()
        noInput.setIcon(icon)
        noInput.setText(message)
        noInput.exec()
