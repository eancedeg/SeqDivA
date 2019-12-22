from Bio import SeqIO
from Bio.Blast.Applications import NcbimakeblastdbCommandline, NcbiblastpCommandline
from PyQt5 import QtCore
import multiprocessing as mp
import pandas as pd
import os
import subprocess as sp


class BlastCalculation(QtCore.QThread):
    onfinished = QtCore.pyqtSignal(pd.DataFrame)

    def __init__(self, matrix_type, fasta):
        QtCore.QThread.__init__(self)

        self.fasta = fasta
        self.matrix_type = matrix_type
        self.cpucount = mp.cpu_count()
        self.type = {'bitscores': 'bitscore', 'raw-scores': 'score', 'identity': 'pident'}

    def run(self):
        num_cases = len(list(SeqIO.parse(self.fasta, 'fasta')))

        # Make Database
        clinedb = NcbimakeblastdbCommandline(cmd='makeblastdb', dbtype='prot', input_file=self.fasta,
                                             input_type='fasta', out=self.fasta)
        clinedb()

        # Calculation
        # clinec = NcbiblastpCommandline(cmd='blastp', query=self.fasta, db=self.fasta, evalue=10,
        #                                outfmt='6 qseqid sseqid pident bitscore score', max_target_seqs=num_cases,
        #                                max_hsps=1, num_threads=self.cpucount, out='all_vs_all.tsv')
        #clinec()
        cmd = 'blastp -out all_vs_all.tsv -outfmt "6 qseqid sseqid pident bitscore score" -query {0} -db {0} ' \
              '-evalue 10 -max_target_seqs {1} -max_hsps 1 -num_threads {2}'.format(self.fasta, num_cases,
                                                                                    self.cpucount)
        sp.call(cmd, shell=True)
        #print(clinec)

        # Data Processing
        data = pd.read_csv('all_vs_all.tsv', delimiter='\t', names=['seq1', 'seq2', 'pident', 'bitscore', 'score'])
        pivoted = data.pivot(index='seq1', columns='seq2', values=self.type[self.matrix_type])

        os.remove('all_vs_all.tsv')
        os.remove('{}.phr'.format(self.fasta))
        os.remove('{}.pin'.format(self.fasta))
        os.remove('{}.psq'.format(self.fasta))

        pivoted_rounded = pivoted.round(2)

        self.onfinished.emit(pivoted_rounded)
