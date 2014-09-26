#!/usr/bin/python
import argparse
import subprocess
from os.path import isfile

HG_19_FILENAME = 'hg19.fa'

def parseArgs():
    parser = argparse.ArgumentParser('easier interface for bowtie2 alignments')
    parser.add_argument('input_fasta', help='the fasta containing the sequences to align')
    parser.add_argument('-a', '--all', help='specify the a flag to list all alignments', action='store_true')
    return parser.parse_args()

def main():
    options = parseArgs()
    fasta_filename = options.input_fasta
    try:
        #ensure the fasta file exists
        if not isfile(fasta_filename):
            print 'file "{}" does not exist'.format(fasta_filename)
            exit(-1)

        #create a hash of the header and the sequence data for later querying
        fastaDict = {}
        with open(fasta_filename) as fasta_file:
            fasta = None
            header = ''
            for line in fasta_file:
                line = line.rstrip()
                if line[0] is '>':
                    header = line[1:]
                    fastaDict[header] = ''
                    continue
                fastaDict[header] += line

        command = './bowtie2 -x {} --very-sensitive -a -f {} | grep AS'.format(HG_19_FILENAME, fasta_filename)
        #get all the alignments
        alignments = subprocess.check_output(command, shell=True)
        #collect and sort by sequence header
        collated_alignments = {}
        for alignment in alignments.split('\n'):
            tokens = alignment.split('\t')
            sequence_header = tokens[0]
            alignment_data = '\t'.join(tokens[1:])
            if sequence_header in collated_alignments:
                collated_alignments[sequence_header].append(alignment_data)
            else:
                collated_alignments[sequence_header] = [alignment_data]

        #print results
        if options.all:
            print 'all allignments:'
            print alignments
        #print multiples
        for header in collated_alignments.keys():
            all_alignments = collated_alignments[header]
            number_alignments = len(all_alignments)
            if number_alignments > 1:
                print 'sequence {} (original sequence = {}) has {} alignments'\
                    .format(header, fastaDict[header], number_alignments)
                for alignment in all_alignments:
                    print alignment
                print '\n'
    except Exception as e:
        print('Warning: Exception during execution: {}'.format(e))
        exit(-1)

if __name__ == '__main__':
    main()