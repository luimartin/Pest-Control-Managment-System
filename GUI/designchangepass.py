# Form implementation generated from reading ui file 'changepassword.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_changePassword(object):
    def setupUi(self, changePassword):
        changePassword.setObjectName("changePassword")
        changePassword.setEnabled(True)
        changePassword.resize(357, 299)
        changePassword.setMinimumSize(QtCore.QSize(357, 299))
        changePassword.setMaximumSize(QtCore.QSize(357, 299))
        changePassword.setStyleSheet("QLineEdit{\n"
"background-color: rgb(144, 206, 103)\n"
"}")
        changePassword.setSizeGripEnabled(False)
        self.changePassSubmitBtn_2 = QtWidgets.QPushButton(parent=changePassword)
        self.changePassSubmitBtn_2.setGeometry(QtCore.QRect(210, 250, 111, 31))
        self.changePassSubmitBtn_2.setStyleSheet("border: none;\n"
"background-color: rgb(0, 255, 0);\n"
"font-size: 14px;\n"
"\n"
"")
        self.changePassSubmitBtn_2.setObjectName("changePassSubmitBtn_2")
        self.layoutWidget = QtWidgets.QWidget(parent=changePassword)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 291, 192))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(17)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.titleLabel.setStyleSheet("")
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.titleLabel)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("color:#005D0F")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_3)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)

        self.retranslateUi(changePassword)
        QtCore.QMetaObject.connectSlotsByName(changePassword)

    def retranslateUi(self, changePassword):
        _translate = QtCore.QCoreApplication.translate
        changePassword.setWindowTitle(_translate("changePassword", "Change Password"))
        self.changePassSubmitBtn_2.setText(_translate("changePassword", "Submit"))
        self.titleLabel.setText(_translate("changePassword", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">HomeFix Pest and Termite Control </span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Managment System</span></p></body></html>"))
        self.label_3.setText(_translate("changePassword", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Validated!</span></p></body></html>"))
        self.label.setText(_translate("changePassword", "New Password:"))
        self.label_2.setText(_translate("changePassword", "Confirm Password:"))
