#!/usr/bin/python
import argparse
import subprocess
HG_19_FILENAME = 'hg19.fa'

def parseArgs():
    parser = argparse.ArgumentParser('easier interface for bowtie2 alignments')
    parser.add_argument('sequence', help='the sequence to align')
    return parser.parse_args()

def main():
    options = parseArgs()
    sequence = options.sequence
    try:
        command = './bowtie2 -x {} --very-sensitive -a -c {} | grep AS ' \
                  '| cut -f3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20'.format(HG_19_FILENAME, sequence)
        print subprocess.check_output(command, shell=True)

    except Exception as e:
        print('Exception aligning: {}'.format(e))

if __name__ == '__main__':
    main()