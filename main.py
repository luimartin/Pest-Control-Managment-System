from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI.LogInUI import Window

   


app = QApplication([])
window = Window()
window.show()
app.exec()