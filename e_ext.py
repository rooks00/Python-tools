'''
This script extracts emails of a particular domain (eg: gmail.com, yahoo.com) from a list of emails.
The list provided as input must contain only 1 email in 1 line.

* Usage: python e_ext.py input.txt output.txt @domain
* Example: python e_ext.py email.txt result.txt @gmail.com
'''

#Importing sys module to use arguments from command line
import sys

#Check whether all the required arguments are given or not.
try:
	#Assigning variables to arguments
	in_file = sys.argv[1]
	out_file = sys.argv[2]
	site = sys.argv[3]
	
	#Opening Input and output files
	infile = open(in_file, "r")
	outfile = open(out_file, "a+")
	
	#Looping through the file one line at a time
	for a in infile:
		#Condition for checking domain name in Email address
		if (site in a):
			#Writing Emails to output file
			outfile.write(a)
	
	#Closing the files to preserver changes
	outfile.close()
	infile.close()

#If all the arguments are not given, then print the Usage with example
except:
	print "Usage: python e_ext.py input.txt output.txt @domain"
	print "Example: python e_ext.py email.txt result.txt @gmail.com"

