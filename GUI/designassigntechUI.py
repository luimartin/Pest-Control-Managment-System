
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(496, 271)
        self.label_5 = QtWidgets.QLabel(parent=dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 120, 121, 21))
        self.label_5.setObjectName("label_5")
        self.techbox = QtWidgets.QComboBox(parent=dialog)
        self.techbox.setGeometry(QtCore.QRect(40, 160, 411, 22))
        self.techbox.setObjectName("techbox")
        self.cancelBtn = QtWidgets.QPushButton(parent=dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(230, 220, 75, 24))
        self.cancelBtn.setObjectName("cancelBtn")
        self.confirBtn = QtWidgets.QPushButton(parent=dialog)
        self.confirBtn.setGeometry(QtCore.QRect(360, 220, 75, 24))
        self.confirBtn.setObjectName("confirBtn")
        self.techbox_2 = QtWidgets.QComboBox(parent=dialog)
        self.techbox_2.setGeometry(QtCore.QRect(40, 80, 411, 22))
        self.techbox_2.setObjectName("techbox_2")
        self.label_6 = QtWidgets.QLabel(parent=dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 121, 21))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.label_5.setText(_translate("dialog", "Assign Technician:"))
        self.cancelBtn.setText(_translate("dialog", "Cancel"))
        self.confirBtn.setText(_translate("dialog", "Confirm"))
        self.label_6.setText(_translate("dialog", "Schedule:"))
