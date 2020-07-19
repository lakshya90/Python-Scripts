import sys, getopt
from random import randint
import time, random
import hashlib
def main(argv):
	inputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:",["ifile="])
	except getopt.GetoptError:
		print ('randomize_file.py -i <inputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('randomize_file.py -i <inputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
	lines = open(inputfile).readlines()
	random.shuffle(lines)
	open(inputfile,'w').writelines(lines)

if __name__ == "__main__":
        a = time.perf_counter()
        main(sys.argv[1:])
        b = time.perf_counter()
        print("Time taken to execute code is "+ str(b-a) + " seconds")


