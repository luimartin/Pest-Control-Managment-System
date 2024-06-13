from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_addClients(object):
    def setupUi(self, addClients):
        addClients.setObjectName("addClients")
        addClients.resize(548, 489)
        addClients.setStyleSheet("QPushButton{\n"
"    height:100%\n"
"}\n"
"")
        self.widget = QtWidgets.QWidget(parent=addClients)
        self.widget.setGeometry(QtCore.QRect(60, 190, 190, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.phonenumInput = QtWidgets.QLineEdit(parent=self.widget)
        self.phonenumInput.setObjectName("phonenumInput")
        self.horizontalLayout_3.addWidget(self.phonenumInput)
        self.widget1 = QtWidgets.QWidget(parent=addClients)
        self.widget1.setGeometry(QtCore.QRect(70, 120, 190, 24))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.emailInput = QtWidgets.QLineEdit(parent=self.widget1)
        self.emailInput.setObjectName("emailInput")
        self.horizontalLayout_2.addWidget(self.emailInput)
        self.widget2 = QtWidgets.QWidget(parent=addClients)
        self.widget2.setGeometry(QtCore.QRect(60, 240, 190, 24))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.widget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.addressInput = QtWidgets.QLineEdit(parent=self.widget2)
        self.addressInput.setObjectName("addressInput")
        self.horizontalLayout_4.addWidget(self.addressInput)
        self.widget3 = QtWidgets.QWidget(parent=addClients)
        self.widget3.setGeometry(QtCore.QRect(80, 60, 190, 24))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameInput = QtWidgets.QLineEdit(parent=self.widget3)
        self.nameInput.setObjectName("nameInput")
        self.horizontalLayout.addWidget(self.nameInput)
        self.widget4 = QtWidgets.QWidget(parent=addClients)
        self.widget4.setGeometry(QtCore.QRect(240, 390, 241, 41))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cancelBtn = QtWidgets.QPushButton(parent=self.widget4)
        self.cancelBtn.setStyleSheet("QPushButton{\n"
"border: none;\n"
"background-color: #E35C5C;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(211, 79, 79);\n"
"    \n"
"}")
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_5.addWidget(self.cancelBtn)
        self.addclientBtn = QtWidgets.QPushButton(parent=self.widget4)
        self.addclientBtn.setStyleSheet("QPushButton{border: none;\n"
"background-color: rgb(0, 255, 0);\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #5CE371\n"
"}")
        self.addclientBtn.setObjectName("addclientBtn")
        self.horizontalLayout_5.addWidget(self.addclientBtn)

        self.retranslateUi(addClients)
        QtCore.QMetaObject.connectSlotsByName(addClients)

    def retranslateUi(self, addClients):
        _translate = QtCore.QCoreApplication.translate
        addClients.setWindowTitle(_translate("addClients", "Dialog"))
        self.label_3.setText(_translate("addClients", "PhoneNumber"))
        self.label_2.setText(_translate("addClients", "Email"))
        self.label_4.setText(_translate("addClients", "Address"))
        self.label.setText(_translate("addClients", "Name"))
        self.cancelBtn.setText(_translate("addClients", "Cancel"))
        self.addclientBtn.setText(_translate("addClients", "Add Client"))
