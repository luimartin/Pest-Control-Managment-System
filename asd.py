import sys
from PyQt6.QtWidgets import QApplication, QDialog, QFormLayout, QComboBox, QLineEdit,QPushButton

class MaterialDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Material")

        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.combo_box = QComboBox()
        self.combo_box.addItem("Mouse Trap")
        self.combo_box.addItem("RAt Trap")
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_changed)
        self.layout.addRow("Material:", self.combo_box)

        self.submit_button = QPushButton("Submit")
        self.layout.addRow("", self.submit_button)

    def on_combo_box_changed(self, index):
        if index == 1:  # Assuming the first item is selected
            self.quantity_edit = QLineEdit()
            self.layout.insertRow(1, "Quantity:", self.quantity_edit)
        else:
            self.layout.removeRow(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MaterialDialog()
    dialog.show()
    sys.exit(app.exec())