
from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(507, 512)
        self.label_11 = QtWidgets.QLabel(parent=Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 281, 81))
        self.label_11.setLineWidth(0)
        self.label_11.setScaledContents(False)
        self.label_11.setIndent(3)
        self.label_11.setObjectName("label_11")
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 90, 421, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(18)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.q1Input = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.q1Input.setObjectName("q1Input")
        self.gridLayout.addWidget(self.q1Input, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.ans2Input = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.ans2Input.setObjectName("ans2Input")
        self.gridLayout.addWidget(self.ans2Input, 4, 1, 1, 1)
        self.ans1Input = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.ans1Input.setObjectName("ans1Input")
        self.gridLayout.addWidget(self.ans1Input, 2, 1, 1, 1)
        self.q2Input = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.q2Input.setObjectName("q2Input")
        self.gridLayout.addWidget(self.q2Input, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.submitBtn = QtWidgets.QPushButton(parent=Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(370, 450, 75, 24))
        self.submitBtn.setObjectName("submitBtn")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(270, 450, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; color:#000000;\">Edit Admin</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "Answer 2"))
        self.label_6.setText(_translate("Dialog", "Answer 1"))
        self.label_7.setText(_translate("Dialog", "Question 2"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_5.setText(_translate("Dialog", "Question 1"))
        self.submitBtn.setText(_translate("Dialog", "Submit"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))

from PyQt6.QtWidgets import QDialog,QMessageBox, QApplication
from user import User

# if edit tangalin yung runner dito
class EditAdmin(QDialog, Ui_Dialog):
    def __init__(self, admin):
        super().__init__()
        self.setupUi(self)
        self.user = User()
        self.admin = admin
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.submitBtn.clicked.connect(self.edit)
        for sec in self.user.security_question:
            self.q1Input.addItem(sec)
            self.q2Input.addItem(sec)


        result = self.user.show_id()
        for row in result:
            user_id, username = row
            self.comboBox.addItem(f"({user_id}) {username}", user_id)
        self.comboboxchange()
        #print(self.user.get_data(self.comboBox.currentData(), 'question1, answer1, question2, answer2')[0][0])
        self.comboBox.currentIndexChanged.connect(self.comboboxchange)

    def comboboxchange(self):
        placeholder = self.user.get_data(self.comboBox.currentData(), 
                            'question1, answer1, question2, answer2')
        #print(placeholder)
        self.q1Input.setCurrentText(placeholder[0][0])
        self.q2Input.setCurrentText(placeholder[0][2])
        self.ans1Input.setText(placeholder[0][1])
        self.ans2Input.setText(placeholder[0][3])

    def edit(self):
        user = self.comboBox.currentData()
        q1 = self.q1Input.currentText()
        q2 = self.q2Input.currentText()
        a1 = self.ans1Input.text()
        a2 = self.ans2Input.text()
        self.user.edit_user(user, 'question1', q1)
        self.user.edit_user(user, 'question2', q2)
        self.user.edit_user(user, 'answer1', a1)
        self.user.edit_user(user, 'answer2', a2)
        self.user.add_backlogs(self.admin, "Edited Admin")
        self.notif("Admin Edited", QMessageBox.Icon.Information)
        self.close()
    def notif(self, message, icon):
        #QMessageBox.Icon.Information
        noInput = QMessageBox()
        noInput.setIcon(icon)
        noInput.setText(message)
        noInput.exec()

