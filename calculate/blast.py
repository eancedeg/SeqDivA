from Bio import SeqIO
from Bio.Blast.Applications import NcbimakeblastdbCommandline, NcbiblastpCommandline
from PyQt5 import QtCore
import multiprocessing as mp
import pandas as pd
import os


class BlastCalculation(QtCore.QThread):
    onfinished = QtCore.pyqtSignal(pd.DataFrame)

    def __init__(self, matrix_type, fasta):
        QtCore.QThread.__init__(self)

        self.fasta = fasta
        self.matrix_type = matrix_type
        self.cpucount = mp.cpu_count()
        self.type = {'bitscores': 'bitscore', 'raw-scores': 'score', 'identity': 'pident'}

    def clean_duplicates(self, raw_data):

        raw_data['check_string'] = raw_data.apply(lambda row: ''.join(sorted([row['seq1'], row['seq2']])), axis=1)
        no_dups = raw_data.drop_duplicates('check_string')
        no_dups.index = pd.RangeIndex(start=1, stop=len(no_dups.index) + 1)

        return no_dups

    def run(self):
        num_cases = len(list(SeqIO.parse(self.fasta, 'fasta')))

        # Make Database
        clinedb = NcbimakeblastdbCommandline(cmd='makeblastdb', dbtype='prot', input_file=self.fasta,
                                             input_type='fasta', out=self.fasta)
        clinedb()

        # Calculation
        clinec = NcbiblastpCommandline(cmd='blastp', query=self.fasta, db=self.fasta, evalue=10,
                                       outfmt='6 qseqid sseqid pident evalue bitscore score', max_target_seqs=num_cases,
                                       max_hsps=1, num_threads=self.cpucount, out='all_vs_all.tsv')
        clinec()

        # Data Processing
        data = pd.read_csv('all_vs_all.tsv', delimiter='\t', names=['seq1', 'seq2', 'pident', 'evalue', 'bitscore',
                                                                    'score'])
        no_dups = self.clean_duplicates(data)
        pivoted = no_dups.pivot(index='seq1', columns='seq2', values=self.type[self.matrix_type])

        for column in pivoted.columns:
            pos = pivoted.index.get_loc(column) + 1
            for index in pivoted.index[pos:]:
                if column != index:
                    pivoted.loc[index, column] = pivoted.loc[column, index]

        os.remove('all_vs_all.tsv')
        os.remove('{}.phr'.format(self.fasta))
        os.remove('{}.pin'.format(self.fasta))
        os.remove('{}.psq'.format(self.fasta))

        pivoted_round = pivoted.round(2)

        self.onfinished.emit(pivoted_round)
