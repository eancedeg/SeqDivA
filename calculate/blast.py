from Bio import SeqIO
from Bio.Blast.Applications import NcbimakeblastdbCommandline, NcbiblastpCommandline
from PyQt5 import QtCore
import multiprocessing as mp
import pandas as pd
import os


class BlastCalculation(QtCore.QThread):
    onfinished = QtCore.pyqtSignal(pd.DataFrame)
    onincompletedata = QtCore.pyqtSignal(str)
    onblastincomplete = QtCore.pyqtSignal(str)

    def __init__(self, matrix_type, fasta):
        QtCore.QThread.__init__(self)

        self.fasta = fasta
        self.matrix_type = matrix_type
        self.cpucount = mp.cpu_count()
        self.type = {'bitscores': 'bitscore', 'raw-scores': 'score', 'identity': 'pident'}

    def modify_id(self, seqs):
        for seqindex in range(len(seqs)):
            seq = seqs[seqindex]
            seq.id = '_'.join(seq.description.split())
            seqs[seqindex] = seq
        return seqs

    def run(self):
        seqs = list(SeqIO.parse(self.fasta, 'fasta'))
        num_cases = len(list(seqs))
        unique_cases = len(set([seq.id for seq in seqs]))

        if num_cases > unique_cases:
            seqs = self.modify_id(seqs)
            SeqIO.write(seqs, 'temp.fasta', 'fasta')
            self.fasta = 'temp.fasta'
            #actual_cases = len(set([seq.id for seq in seqs]))

        #     if num_cases == actual_cases:
        # Make Database
        clinedb = NcbimakeblastdbCommandline(cmd='makeblastdb', dbtype='prot', input_file=self.fasta,
                                             input_type='fasta', out=self.fasta, parse_seqids=True)
        clinedb()

        # Calculation
        clinec = NcbiblastpCommandline(cmd='blastp', query=self.fasta, db=self.fasta, evalue=0.1,
                                       outfmt='6 qseqid sseqid pident evalue bitscore score',
                                       max_target_seqs=num_cases, max_hsps=1, num_threads=self.cpucount,
                                       out='all_vs_all.tsv')
        clinec()

        # Data Processing
        data = pd.read_csv('all_vs_all.tsv', delimiter='\t', names=['seq1', 'seq2', 'pident', 'evalue',
                                                                    'bitscore', 'score'])
        pivoted = data.pivot(index='seq1', columns='seq2', values=self.type[self.matrix_type])

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
            # elif num_cases > actual_cases:
            #     self.onincompletedata.emit('Duplicate sequences in "fasta"')
            # else:
            #     self.onblastincomplete.emit("El blast no completó el total de los casos")
