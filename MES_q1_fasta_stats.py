from Bio import SeqIO
import re

## the name of the input file 
file = "sample_sequences.fasta"

# Set up variables to act as counters for each statistic
seq_count = 0
base_count = 0
longest = 0
np_count = 0
pattern_count = 0

# loop over the sequences in the file using biopython
for seq_record in SeqIO.parse(file, "fasta"):
        # add our current sequence to the running total of sequences
	seq_count += 1

        # add the length of our current sequence to the running total bases
	bases = str(seq_record.seq)
	base_count += len(bases)

        # is this the longest seen so far? If so update longest variable
	if len(bases) > longest:
		longest = len(bases)

        # check if name starts with NM_00, update tally if so
	if re.search(r"^NM_00", seq_record.id):
		np_count += 1
                
        # check if sequence has RE ATRWGC, update tally if so
	if re.search(r"AT(A|G)(A|T)GC", bases):
		pattern_count += 1

# Use the total bases and sequences to calculate the average seq length
average_len = base_count/seq_count

# print all statistics to terminal
print("The number of sequences is: " + str(seq_count))
print("The number of bases is: " + str(base_count))
print("The average sequence length is: " + (str(average_len)))
print("The longest sequence : " + str(longest))
print("The number of sequences beginning with NM_00 is : " + str(np_count))
print("The number of sequences with an ATRWGC cut site is : " + str(pattern_count))
