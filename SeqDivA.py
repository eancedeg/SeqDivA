import sys
from PyQt5 import QtCore, QtWidgets
from ui.SeqDivAGUI import Ui_SeqDivA
from ui.MatrixGUI import MatrixWin
from Bio import SeqIO
from calculate.FileManager import matrix_header, data_extractor, cuadrate_matrix
import numpy as np
import os


class Calculation(QtCore.QThread):
    progress = QtCore.pyqtSignal(int)
    prog_range = QtCore.pyqtSignal(int)
    onfinished = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, method, fasta):
        QtCore.QThread.__init__(self)

        self.fasta = fasta
        self.method = method

    def run(self):
        alignments = list(SeqIO.parse(self.fasta, 'fasta'))

        header = matrix_header(self.fasta)
        matrix_identity = []
        matrix_similarity = []

        self.prog_range.emit(len(alignments) - 2)

        for case in range(len(alignments) - 1):
            SeqIO.write(alignments[case], 'caso_base.fasta', 'fasta')
            SeqIO.write(alignments[case + 1:], 'resto_casos.fasta', 'fasta')

            command = self.method + ' -auto -asequence=caso_base.fasta -bsequence=resto_casos.fasta -gapopen=10 ' \
                                    '-gapextend=0.5 -outfile=salida.txt'
            os.system(command)

            datos = data_extractor()
            data_identity = [0] * (len(header) - 1 - len(datos[0])) + [100] + datos[0]
            data_similarity = [0] * (len(header) - 1 - len(datos[1])) + [100] + datos[1]
            matrix_identity.append(data_identity)
            matrix_similarity.append(data_similarity)

            os.remove('caso_base.fasta')
            os.remove('resto_casos.fasta')
            os.remove('salida.txt')
            self.progress.emit(case)

        matrix_identity.append([0] * (len(header) - 1) + [100])
        matrix_similarity.append([0] * (len(header) - 1) + [100])
        self.onfinished.emit(np.array([cuadrate_matrix(matrix_identity), cuadrate_matrix(matrix_similarity)]))


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_SeqDivA()
        self.ui.setupUi(self)

        # Variables
        self.calculation_method = 'needle'
        self.file = ''
        self.matrix_type = 'similarity'
        self.resultados = []

        # Threads
        self.threadWorker = Calculation(self.calculation_method, self.file)

        # Events
        self.ui.actionOpen_Fasta.triggered.connect(self.openfasta)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.water.triggered.connect(self.wateraction)
        self.ui.needle.triggered.connect(self.needleaction)
        self.ui.identity.triggered.connect(self.identityaction)
        self.ui.similarity.triggered.connect(self.similarityaction)
        self.ui.calculate.clicked.connect(self.calculate)
        self.threadWorker.prog_range.connect(self.progressrange)
        self.threadWorker.progress.connect(self.setprogress)
        self.threadWorker.onfinished.connect(self.results)

    def setprogress(self, i):
        self.ui.progressBar.setValue(i)

    def progressrange(self, i):
        self.ui.progressBar.setRange(0, i)

    def openfasta(self):
        file, ok = QtWidgets.QFileDialog.getOpenFileName(self, 'Select .fasta file:', '',
                                                         'Fasta files (*.fasta);; All files (*)')
        if file:
            self.file = file
            with open(file) as fasta:
                self.ui.FastaText.setText(fasta.read())

    def clear(self):
        self.ui.FastaText.setText('')

    def wateraction(self):
        self.ui.needle.setChecked(False)
        self.calculation_method = 'water'

    def needleaction(self):
        self.ui.water.setChecked(False)
        self.calculation_method = 'needle'

    def identityaction(self):
        self.ui.similarity.setChecked(False)
        self.ui.calculate.setText('Calculate Identity')
        self.matrix_type = 'identity'

    def similarityaction(self):
        self.ui.actionIdentity.setChecked(False)
        self.ui.similarity.setChecked(True)
        self.ui.calculate.setText('Calculate Similarity')
        self.matrix_type = 'similarity'

    def calculate(self):
        self.ui.calculate.setDisabled(True)
        self.threadWorker.fasta = self.file
        self.threadWorker.method = self.calculation_method
        self.threadWorker.start()

    def results(self, result):
        matrix = MatrixWin()
        if self.matrix_type == 'similarity':
            matrix.filltable(result[1])
            matrix.data = result[1]
        elif self.matrix_type == 'identity':
            matrix.filltable(result[0])
            matrix.data = result[0]

        matrix.exec_()
        self.ui.calculate.setDisabled(False)
        self.ui.progressBar.setValue(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window(None)
    win.show()
    sys.exit(app.exec_())
