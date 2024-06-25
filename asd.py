import sys
import matplotlib
matplotlib.use('QtAgg')

from PyQt6 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class SaleTrendDialog(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super(SaleTrendDialog, self).__init__(*args, **kwargs)

        # Create the matplotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        # Set up the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        self.setLayout(layout)

        self.setWindowTitle("Matplotlib Plot in QDialog")
        self.resize(600, 400)