bowtie2_alignment_wrapper
=========================

a wrapper for finding alignments using bowtie2

To align a fasta file:

		./fasta_align.py ignyta_0.8_gsp1.fasta
	
	where 'ignyta_0.8_gsp1.fasta' is the name of the fasta you want to align. The './' means 'run this file'. 
	Additionally, you can specify the '-a' flag to print all alignments, not just those with multiple hits. 
		
		./fasta_align.py -a ignyta_0.8_gsp1.fasta
		
To align a sequence:
		
		./sequence_align.py CCATCCTCCTCCTTTTCCTCCTCCC
		
