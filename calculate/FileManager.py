import os
import numpy
from Bio import SeqIO
import re

def splitrose(file):
    rose = open(file, 'r')
    ruta = os.path.split(file)[0]
    basename = os.path.splitext(os.path.split(file)[1])[0]
    fasta = open(os.path.join(ruta, basename + '.fasta'), 'w')
    phylip = open(os.path.join(ruta, basename + '.phy'), 'w')
    line = rose.readline()
    fasta_init = 0
    fasta_end = 0
    phylip_init = 0
    while line:
        if 'Sequences' in line:
            fasta_init = rose.tell()
        if 'Alignment' in line:
            fasta_end = rose.tell() - len(line)
        if 'PHYLIP tree' in line:
            phylip_init = rose.tell()

        line = rose.readline()

    rose.seek(fasta_init)
    print >> fasta, rose.read(fasta_end - fasta_init).rstrip()
    rose.seek(phylip_init)
    print >> phylip, rose.read().rstrip()

    rose.close()
    fasta.close()
    phylip.close()

def data_extractor():

    fichero = open('salida.txt', 'r')

    Identity = []
    Similarity = []

    for linea in fichero:
        if 'Identity' in linea:
            Identity.append(float(re.findall(r"(\d+\.\d+)", linea.split()[-1])[0]))
        elif 'Similarity' in linea:
            Similarity.append(float(re.findall(r"(\d+\.\d+)", linea.split()[-1])[0]))
    return [Identity, Similarity]

def matrix_header(fichero):
    header = []
    alin = list(SeqIO.parse(fichero, 'fasta'))
    for case in alin:
        header.append(case.id)
    return header

def cuadrate_matrix(triangular):
    for i in range(len(triangular)):
        for j in range(i + 1, len(triangular)):
            triangular[j][i] = triangular[i][j]
    return triangular

def generate_matrix(file, method):
    alignments = list(SeqIO.parse(file, 'fasta'))

    header = matrix_header(file)
    matrix_identity = []
    matrix_similarity = []

    for case in range(len(alignments) - 1):
        SeqIO.write(alignments[case], 'caso_base.fasta', 'fasta')
        SeqIO.write(alignments[case + 1:], 'resto_casos.fasta', 'fasta')

        command = method + ' -auto -asequence=caso_base.fasta -bsequence=resto_casos.fasta -gapopen=10 -gapextend=0.5 -outfile=salida.txt'
        os.system(command)

        datos = data_extractor()
        data_identity = [0] * (len(header) - 1 - len(datos[0])) + [100] + datos[0]
        data_similarity = [0] * (len(header) - 1 - len(datos[1])) + [100] + datos[1]
        matrix_identity.append(data_identity)
        matrix_similarity.append(data_similarity)

        os.remove('caso_base.fasta')
        os.remove('resto_casos.fasta')
        os.remove('salida.txt')


    matrix_identity.append([0] * (len(header) - 1) + [100])
    matrix_similarity.append([0] * (len(header) - 1) + [100])
    return numpy.array([cuadrate_matrix(matrix_identity), cuadrate_matrix(matrix_similarity)])
