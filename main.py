from PyQt6.QtWidgets import QApplication
from GUI.LogInUI import Window
from database import *

app = QApplication([])
window = Window()
window.show()
app.exec()