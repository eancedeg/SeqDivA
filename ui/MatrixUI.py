# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatrixUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MatrixW(object):
    def setupUi(self, MatrixW):
        MatrixW.setObjectName("MatrixW")
        MatrixW.resize(518, 368)
        self.verticalLayout = QtWidgets.QVBoxLayout(MatrixW)
        self.verticalLayout.setObjectName("verticalLayout")
        self.matrix = QtWidgets.QTableWidget(MatrixW)
        self.matrix.setEnabled(True)
        self.matrix.setAlternatingRowColors(True)
        self.matrix.setRowCount(3)
        self.matrix.setColumnCount(2)
        self.matrix.setObjectName("matrix")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.matrix.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.matrix.setItem(0, 1, item)
        self.verticalLayout.addWidget(self.matrix)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.save = QtWidgets.QPushButton(MatrixW)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.dotplot = QtWidgets.QPushButton(MatrixW)
        self.dotplot.setObjectName("dotplot")
        self.horizontalLayout.addWidget(self.dotplot)
        self.close = QtWidgets.QPushButton(MatrixW)
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MatrixW)
        self.close.clicked.connect(MatrixW.close)
        QtCore.QMetaObject.connectSlotsByName(MatrixW)
        MatrixW.setTabOrder(self.save, self.dotplot)
        MatrixW.setTabOrder(self.dotplot, self.close)

    def retranslateUi(self, MatrixW):
        _translate = QtCore.QCoreApplication.translate
        MatrixW.setWindowTitle(_translate("MatrixW", "Alignment Matrix"))
        __sortingEnabled = self.matrix.isSortingEnabled()
        self.matrix.setSortingEnabled(False)
        item = self.matrix.item(0, 0)
        item.setText(_translate("MatrixW", "7"))
        item = self.matrix.item(0, 1)
        item.setText(_translate("MatrixW", "8"))
        self.matrix.setSortingEnabled(__sortingEnabled)
        self.save.setText(_translate("MatrixW", "Save"))
        self.dotplot.setText(_translate("MatrixW", "DotPlot"))
        self.close.setText(_translate("MatrixW", "Close"))

