# import required modules
from Bio import SeqIO
import re

# initiate different counters for different outputs
line_counter = 0
bases_counter = 0
nm_counter = 0
atrwgc_counter = 0
list_of_sequences = []

# initiate for loop using parse method from Biopython
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
	header = seq_record.id
	seq = str(seq_record.seq)
	# update the line count
	line_counter += 1
	dna_length = len(seq)
	# update the number of total bases
	bases_counter += dna_length
	# create a list of sequences
	list_of_sequences.append(seq)
	# if "ATRWGC" is found, add 1 to the counter
	if re.search(r"AT[AG][AT]GC", seq):
		atrwgc_counter += 1
	# if sequence id starts with '>NM_00' add 1 to its counter
	if header.startswith('>NM_00'):
		nm_counter += 1

avg_length = round(bases_counter/line_counter, 2)

# sort the list of sequences according to their length such that last sequence is the longest sequence
sorted_list = sorted(list_of_sequences, key = len)

# length of longest sequence
len_longest_seq = len(sorted_list[-1])

print("The number of sequences is: " + str(line_counter))
print("The number of bases is: " + str(bases_counter))
print("The average sequence length is: " + str(avg_length)) 
print("The length of longest sequence is: " + str(len_longest_seq))
print("The number of sequences beginning with >NM_00 is: " + str(nm_counter))
print("The number of sequences with the an ATRWGC cut site is: " + str(atrwgc_counter))

