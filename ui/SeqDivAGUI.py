# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SeqDivAGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SeqDivA(object):
    def setupUi(self, SeqDivA):
        SeqDivA.setObjectName("SeqDivA")
        SeqDivA.resize(696, 430)
        self.centralwidget = QtWidgets.QWidget(SeqDivA)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FastaText = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setBold(True)
        font.setWeight(75)
        self.FastaText.setFont(font)
        self.FastaText.setLineWrapColumnOrWidth(80)
        self.FastaText.setReadOnly(True)
        self.FastaText.setAcceptRichText(False)
        self.FastaText.setObjectName("FastaText")
        self.verticalLayout.addWidget(self.FastaText)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setObjectName("calculate")
        self.horizontalLayout.addWidget(self.calculate)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout.addWidget(self.Close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.protein = QtWidgets.QRadioButton(self.groupBox_2)
        self.protein.setGeometry(QtCore.QRect(12, 30, 68, 21))
        self.protein.setChecked(True)
        self.protein.setObjectName("protein")
        self.dna = QtWidgets.QRadioButton(self.groupBox_2)
        self.dna.setGeometry(QtCore.QRect(86, 30, 53, 21))
        self.dna.setObjectName("dna")
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.similarity = QtWidgets.QRadioButton(self.groupBox)
        self.similarity.setChecked(True)
        self.similarity.setObjectName("similarity")
        self.horizontalLayout_2.addWidget(self.similarity)
        self.actionIdentity = QtWidgets.QRadioButton(self.groupBox)
        self.actionIdentity.setObjectName("actionIdentity")
        self.horizontalLayout_2.addWidget(self.actionIdentity)
        self.actionbitscores = QtWidgets.QRadioButton(self.groupBox)
        self.actionbitscores.setEnabled(False)
        self.actionbitscores.setObjectName("actionbitscores")
        self.horizontalLayout_2.addWidget(self.actionbitscores)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        SeqDivA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SeqDivA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMatrix = QtWidgets.QMenu(self.menubar)
        self.menuMatrix.setObjectName("menuMatrix")
        self.menuMatrixtype = QtWidgets.QMenu(self.menuMatrix)
        self.menuMatrixtype.setObjectName("menuMatrixtype")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        SeqDivA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SeqDivA)
        self.statusbar.setObjectName("statusbar")
        SeqDivA.setStatusBar(self.statusbar)
        self.actionOpen_Fasta = QtWidgets.QAction(SeqDivA)
        self.actionOpen_Fasta.setObjectName("actionOpen_Fasta")
        self.actionClose = QtWidgets.QAction(SeqDivA)
        self.actionClose.setObjectName("actionClose")
        self.needle = QtWidgets.QAction(SeqDivA)
        self.needle.setCheckable(True)
        self.needle.setChecked(True)
        self.needle.setObjectName("needle")
        self.water = QtWidgets.QAction(SeqDivA)
        self.water.setCheckable(True)
        self.water.setObjectName("water")
        self.actionIdentity1 = QtWidgets.QAction(SeqDivA)
        self.actionIdentity1.setCheckable(True)
        self.actionIdentity1.setObjectName("actionIdentity1")
        self.similarity1 = QtWidgets.QAction(SeqDivA)
        self.similarity1.setCheckable(True)
        self.similarity1.setChecked(True)
        self.similarity1.setObjectName("similarity1")
        self.actionSplit_Rose = QtWidgets.QAction(SeqDivA)
        self.actionSplit_Rose.setObjectName("actionSplit_Rose")
        self.actionAbout = QtWidgets.QAction(SeqDivA)
        self.actionAbout.setObjectName("actionAbout")
        self.blast = QtWidgets.QAction(SeqDivA)
        self.blast.setCheckable(True)
        self.blast.setObjectName("blast")
        self.actionbitscores1 = QtWidgets.QAction(SeqDivA)
        self.actionbitscores1.setCheckable(True)
        self.actionbitscores1.setObjectName("actionbitscores1")
        self.menuFile.addAction(self.actionOpen_Fasta)
        self.menuFile.addAction(self.actionSplit_Rose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuMatrixtype.addAction(self.needle)
        self.menuMatrixtype.addAction(self.water)
        self.menuMatrixtype.addAction(self.blast)
        self.menuMatrix.addAction(self.menuMatrixtype.menuAction())
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMatrix.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(SeqDivA)
        self.Close.clicked.connect(SeqDivA.close)
        self.actionClose.triggered.connect(SeqDivA.close)
        QtCore.QMetaObject.connectSlotsByName(SeqDivA)

    def retranslateUi(self, SeqDivA):
        _translate = QtCore.QCoreApplication.translate
        SeqDivA.setWindowTitle(_translate("SeqDivA", "SeqDivA - Sequence Diversity Analysis"))
        self.calculate.setText(_translate("SeqDivA", "Calculate Similarity"))
        self.clear.setText(_translate("SeqDivA", "Clear"))
        self.Close.setText(_translate("SeqDivA", "Close"))
        self.groupBox_2.setTitle(_translate("SeqDivA", "Input Database"))
        self.protein.setText(_translate("SeqDivA", "Protein"))
        self.dna.setText(_translate("SeqDivA", "DNA"))
        self.groupBox.setTitle(_translate("SeqDivA", "Matrix Type"))
        self.similarity.setText(_translate("SeqDivA", "Similarity"))
        self.actionIdentity.setText(_translate("SeqDivA", "Identity"))
        self.actionbitscores.setText(_translate("SeqDivA", "Bit-Scores"))
        self.menuFile.setTitle(_translate("SeqDivA", "&File"))
        self.menuMatrix.setTitle(_translate("SeqDivA", "Methods"))
        self.menuMatrixtype.setTitle(_translate("SeqDivA", "&Method"))
        self.menuAbout.setTitle(_translate("SeqDivA", "&Help"))
        self.actionOpen_Fasta.setText(_translate("SeqDivA", "Open &Fasta"))
        self.actionOpen_Fasta.setShortcut(_translate("SeqDivA", "Ctrl+F"))
        self.actionClose.setText(_translate("SeqDivA", "&Close"))
        self.actionClose.setShortcut(_translate("SeqDivA", "Ctrl+Q"))
        self.needle.setText(_translate("SeqDivA", "&needle"))
        self.water.setText(_translate("SeqDivA", "&water"))
        self.actionIdentity1.setText(_translate("SeqDivA", "Identity Matrix"))
        self.similarity1.setText(_translate("SeqDivA", "Similarity Matrix"))
        self.actionSplit_Rose.setText(_translate("SeqDivA", "Split &Rose"))
        self.actionSplit_Rose.setShortcut(_translate("SeqDivA", "Ctrl+R"))
        self.actionAbout.setText(_translate("SeqDivA", "&About"))
        self.blast.setText(_translate("SeqDivA", "blast"))
        self.actionbitscores1.setText(_translate("SeqDivA", "Bit-scores Matrix"))

