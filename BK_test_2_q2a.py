# import required modules
import random

# initiate the function with 3 positional arguments
def run_goostats(k_begin, k_end, reps):
	# initiate an empty list
	output = []
	# iterate over k
	for k in range(k_begin, k_end + 1):
		# iterate over reps for each k value
		for r in range(1, reps + 1):
			# randomly select a number between 0 and 100
			a = random.randrange(0, 100)
			statements = "goostats -K " + str(k) + " -r " + str(a) + " outfile_K_" + str(k) + "_rep" + str(r) + ".txt " + "inputfile"
			# append the statements to the list
			output.append(statements)
	return output

# use the function with specified values
for i in run_goostats(1, 5, 3):
	print(i)
