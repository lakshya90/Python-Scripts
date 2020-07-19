#!/usr/bin/python

import sys, getopt
from random import randint
import time

def main(argv):
	length = ''
	lines = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hl:n:o:",["length=","lines=","ofile="])
	except getopt.GetoptError:
		print ('generate_numbers.py -l <length of each number> -n <number of lines to be generated> -o <output file>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('generate_numbers.py -l <length of each number> -n <number of lines to be generated> -o <output file>')
			sys.exit()
		elif opt in ("-l", "--length"):
			length = int(arg)
		elif opt in ("-n", "--lines"):
			lines = int(arg)
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	
	def random_with_specified_length(n):
    		range_start = 10**(n-1)
    		range_end = (10**n)-1
    		return randint(range_start, range_end)

	f= open(outputfile,"w+")	
	for i in range(lines):
		f.write(str(random_with_specified_length(length))+ '\n')
	f.close()
if __name__ == "__main__":
	a = time.perf_counter()
	main(sys.argv[1:])
	b = time.perf_counter()
	print("Time taken to execute code is "+ str(b-a) + " seconds")
