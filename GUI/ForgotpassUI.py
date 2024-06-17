from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from GUI.designforgotpassUI import Ui_forgotPassword
from GUI.changepassUI import ChangePass
from user import User
from user import User
class ForgotPass(QDialog, Ui_forgotPassword):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.User = User()
        self.changePassSubmitBtn_2.setEnabled(False)
        self.changePassSubmitBtn_2.setVisible(False)
        self.forgotPassCancelBtn.clicked.connect(lambda: self.close())
        self.changePassSubmitBtn.clicked.connect(self.forgotpassHandler)
        self.changePassSubmitBtn_2.clicked.connect(self.questions)
        self.q1label.setVisible(False)
        self.q2label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_7.setVisible(False)
        self.ansInput.setVisible(False)
        self.ans2Input.setVisible(False)

    def forgotpassHandler(self):
        adminID = int(self.adminIDInput.text())
        username = self.usernameInput.text()
        if (adminID and username) == "":
            print(adminID, username)
            self.notif("Please input Admin ID or Username", QMessageBox.Icon.Warning)

        elif self.User.cp_validate_user(adminID, username):
            self.q1label.setVisible(True)
            self.q2label.setVisible(True)
            self.label_2.setVisible(True)
            self.label_4.setVisible(True)
            self.label_5.setVisible(True)
            self.label_7.setVisible(True)
            self.ansInput.setVisible(True)
            self.ans2Input.setVisible(True)
            self.adminID = adminID
            self.changePassSubmitBtn.setEnabled(False)
            self.changePassSubmitBtn.setVisible(False)
            self.changePassSubmitBtn_2.setEnabled(True)
            self.changePassSubmitBtn_2.setVisible(True)
            self.adminIDInput.setVisible(False)
            self.adminIDLabel.setVisible(False)
            self.usernameLabel.setVisible(False)
            self.usernameInput.setVisible(False)
            ques = self.User.get_data(self.adminID, ("question1, question2"))
            self.q1label.setText(ques[0][0])
            self.q2label.setText(ques[0][1])
        else:
            self.notif("Invalid Credential", QMessageBox.Icon.Warning)

    def questions(self):

        a1 = self.ansInput.text()
        a2 = self.ans2Input.text()
        if self.User.cp_questions(self.adminID,a1,a2):
            #validation here 
            self.hide()
            changepass = ChangePass(self.adminID)
            changepass.exec()
            self.close()
        else:
            self.notif("Invalid Answer", QMessageBox.Icon.Warning)

    def notif(self, message, icon):
        noInput = QMessageBox()
        noInput.setIcon(icon)
        noInput.setText(message)
        noInput.exec()


