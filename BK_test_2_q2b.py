# import required modules
import re

# initiate the function with one argument
def molecule_type(string):
	# look for DNA base pairs in the whole string
	if re.match(r"^[ATGC]+$", string):
		return "DNA"
	# look for amino acid in the whole string
	elif re.match(r"^[ACDEFGHIKLMNOPQRSTVWY]+$", string):
		return "Amino Acid"
	else:
		return "Unknown"

# assertion statements
assert molecule_type("AAAA") == "DNA"
assert molecule_type("ACTGGGA") == "DNA"
assert molecule_type("ACTGGGN") == "Amino Acid"
assert molecule_type("NNNNNNN") == "Amino Acid"
assert molecule_type("GHMKL") == "Amino Acid"
assert molecule_type("GHJKL") == "Unknown"
assert molecule_type("RB") == "Unknown"
assert molecule_type("T") == "DNA"
assert molecule_type("TF") == "Amino Acid"

file = open("inputfile.txt")

# iterate the function over the input file
for molecule in file:
	output = molecule_type(molecule)
	print(output)

file.close()

