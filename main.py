from clientinfo import ClientInfo
from technician import Technician
from inventory import Inventory
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI.LogInUI import Window
from user import User
import database
import time

   


app = QApplication([])
window = Window()
window.show()
app.exec()