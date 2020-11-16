import re

# This function takes a single string and returns whether it is DNA, Amino Acid or Unknown
def molecule_type(molecule):
        # DNA is defined as consisting of only A, T, C and G characters
	if re.search(r"^[ACTG]*$", molecule):
		return("DNA")

        # Amino Acid is defined as consisting of only ACDEFGHIKLMNOPQRSTVWY characters
	elif re.search(r"^[ACDEFGHIKLMNOPQRSTVWY]*$", molecule):

		return("Amino Acid")
        # Everything else is Unknown
	else:
		return("Unknown")

# Assertions check if the function is working properly
assert molecule_type("AAAA") == "DNA"
assert molecule_type("ACTGGGA") == "DNA"
assert molecule_type("ACTGGGN") == "Amino Acid"
assert molecule_type("NNNNNNN") == "Amino Acid"
assert molecule_type("GHMKL") == "Amino Acid"
assert molecule_type("GHJKL") == "Unknown"
assert molecule_type("RB") == "Unknown"
assert molecule_type("T") == "DNA"
assert molecule_type("TF") == "Amino Acid"

# Iterate over the input file and determine the molecule type for each sequence (one per line)
fh = open("inputfile.txt")
for line in fh:
	print(molecule_type(line))
