from ui.MatrixUI import Ui_MatrixW
from ui.dotPlotGUI import DotPlot
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtWidgets import QTableWidgetItem
import numpy as np


class MatrixWin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_MatrixW()
        self.ui.setupUi(self)
        self.data = []

        # Events
        self.ui.save.clicked.connect(self.save)
        self.ui.dotplot.clicked.connect(self.dotplot)

    def filltable(self, matrix):
        self.ui.matrix.setRowCount(len(matrix))
        self.ui.matrix.setColumnCount(len(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(str(matrix[i][j]))
                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                self.ui.matrix.setItem(i, j, item)

    def save(self):
        savefile = QtWidgets.QFileDialog()
        savefile.setDefaultSuffix('.csv')
        file, ok = savefile.getSaveFileName(self, 'Save your results...', '.', '.csv (*.csv);; All Files (*)')
        if file:
            if not file.endswith('.csv'):
                np.savetxt('{}.csv'.format(file), self.data, delimiter=',', fmt='%s')
            else:
                np.savetxt(file, self.data, delimiter=',', fmt='%s')

    def dotplot(self):
        dotplot = DotPlot(self.data)
        dotplot.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = MatrixWin(None)
    dialog.show()
    sys.exit(app.exec_())
