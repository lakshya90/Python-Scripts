import sys, getopt
from random import randint
import time
import hashlib
def main(argv):
	inputfile = ''
	outputfile = ''
	salt = ''
	hashalgo = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:s:a:",["ifile=","ofile=","salt=","hashalgo="])
	except getopt.GetoptError:
		print ('hashing_numbers.py -i <inputfile> -o <outputfile> -s <salt> -a <hash algo>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('hashing_numbers.py -i <inputfile> -o <outputfile> -s <salt> -a <hash algo>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-s", "--salt"):
			salt = arg
		elif opt in ("-a", "--hashalgo"):
			hashalgo = arg
	
	i_f = open(inputfile,"r")
	o_f = open(outputfile,"w+")
	temp_file = 'temp_'+outputfile
	t_f = open(temp_file,"w+")
	dict = {}
	for i in i_f:
		if hashalgo == 'md5':	
			hash = hashlib.md5( (salt + i).encode('utf-8')).hexdigest()
			dict[i] = hash
			o_f.write(hash + '\n')
			t_f.write(hash+","+i) 
		elif hashalgo == 'sha256':
			hash = hashlib.sha256((salt + i).encode('utf-8')).hexdigest()
			dict[i] = hash
			o_f.write(hash + '\n')
			t_f.write(hash+","+i)
	i_f.close()
	o_f.close()
	t_f.close()

if __name__ == "__main__":
        a = time.perf_counter()
        main(sys.argv[1:])
        b = time.perf_counter()
        print("Time taken to execute code is "+ str(b-a) + " seconds")


