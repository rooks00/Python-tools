import sys

try:
	in_file = sys.argv[1]
	out_file = sys.argv[2]
	site = sys.argv[3]

	infile = open(in_file, "r")
	outfile = open(out_file, "a+")

	for a in infile:
		if (site in a):
			outfile.write(a)
	outfile.close()
	infile.close()

except:
	print "Usage: python e_ext.py input.txt output.txt @domain"
	print "Example: python e_ext.py email.txt result.txt @gmail.com"

