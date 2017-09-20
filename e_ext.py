'''
This script extracts emails of a particular domain (eg: gmail.com, yahoo.com) from a list of emails.
The list provided as input must contain only 1 email in 1 line.

* Usage: python e_ext.py input.txt output.txt @domain
* Example: python e_ext.py email.txt result.txt @gmail.com
'''

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

