import matplotlib
from matplotlib import pyplot as plt
from matplotlib import cm
from PyQt5 import QtWidgets
import sys
from ui.dotPlot import Ui_Dialog
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
matplotlib.use('Qt5Agg')


class DotPlot(QtWidgets.QDialog):
    def __init__(self, data):
        QtWidgets.QDialog.__init__(self, parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.data = np.array(data)
        self.figure = plt.figure(figsize=(5, 5))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.ui.verticalLayout.insertWidget(0, self.canvas)
        self.ui.verticalLayout.insertWidget(1, self.toolbar)

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        if len(self.data) <= 10:
            ax.set_xticks(range(1, len(self.data) + 1))
            ax.set_xticklabels(range(1, len(self.data) + 1))
            ax.set_yticks(range(1, len(self.data) + 1))
            ax.set_yticklabels(range(1, len(self.data) + 1))
        else:
            ax.set_xticks(np.arange(1, len(self.data) + 1, len(self.data) // 10))
            ax.set_xticklabels(np.arange(1, len(self.data) + 1, (len(self.data)) // 10))
            ax.set_yticks(np.arange(1, len(self.data) + 1, (len(self.data)) // 10))
            ax.set_yticklabels(np.arange(1, len(self.data) + 1, (len(self.data)) // 10))


        # plot data
        im = ax.pcolor(self.data, cmap=cm.jet)
        self.figure.colorbar(im, ax=ax)

        # refresh canvas
        self.canvas.draw()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = DotPlot(None)
    win.show()
    sys.exit(app.exec_())
