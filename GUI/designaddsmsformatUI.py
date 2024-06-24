
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 490)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 49, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 391, 71))
        self.label_9.setLineWidth(0)
        self.label_9.setScaledContents(False)
        self.label_9.setIndent(3)
        self.label_9.setObjectName("label_9")
        self.viewBtn = QtWidgets.QPushButton(parent=Dialog)
        self.viewBtn.setGeometry(QtCore.QRect(40, 390, 111, 24))
        self.viewBtn.setObjectName("viewBtn")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(300, 440, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 440, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 110, 441, 271))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(18)
        self.gridLayout.setVerticalSpacing(14)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.titleInput = QtWidgets.QLineEdit(parent=self.widget)
        self.titleInput.setObjectName("titleInput")
        self.gridLayout.addWidget(self.titleInput, 1, 1, 1, 1)
        self.msgInput = QtWidgets.QTextEdit(parent=self.widget)
        self.msgInput.setObjectName("msgInput")
        self.gridLayout.addWidget(self.msgInput, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt;\">Add SMS Format</span></p><p><br/></p></body></html>"))
        self.viewBtn.setText(_translate("Dialog", "View Tokenizer"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Submit"))
        self.label_2.setText(_translate("Dialog", "Recipient Type:"))
        self.comboBox.setItemText(0, _translate("Dialog", "Client"))
        self.comboBox.setItemText(1, _translate("Dialog", "Technician"))
        self.label_3.setText(_translate("Dialog", "Title:"))

from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designviewtokenUI import ViewToken
from message import Message
class AddSMS(QDialog, Ui_Dialog):
    
    def __init__(self, which, id):
        super().__init__()
        self.setupUi(self)
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.viewBtn.clicked.connect(self.view)
        self.pushButton_3.clicked.connect(self.addsms)
        self.m = Message()
        self.which= which
        self.id = id
        if which == "Edit":
            placeholder = self.m.show_specific(id)
            self.comboBox.setCurrentText(placeholder[0][1])
            self.titleInput.setText(placeholder[0][3])
            self.msgInput.setText(placeholder[0][2])
    def view(self):
        v = ViewToken()
        v.exec()
    
    def addsms(self):
        rtype = self.comboBox.currentText()
        title = self.titleInput.text()
        msg = self.msgInput.toPlainText()
        if self.which == "Edit":
            if (title and msg) == "":
                self.notif(QMessageBox.Icon.Warning, "Field cannot be null!")
            else:
                self.m.edit_message(self.id, rtype, msg, title)
                self.notif(QMessageBox.Icon.Information, "Message Edited")
                self.close()

        else:
            if (title and msg) == "":
                self.notif(QMessageBox.Icon.Warning, "Field cannot be null!")
            else:
                self.m.add_message(rtype, title, msg)
                self.notif(QMessageBox.Icon.Information, "Message Added")
                self.close()
            print(rtype, title, msg)
        
    def notif(self, type, message):
        noInput = QMessageBox()
        noInput.setIcon(type)
        noInput.setText(message)
        noInput.exec()
