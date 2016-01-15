# pip install pydub
import sys, random

ifile = sys.argv[1]
outfile = ifile + '_cutup.txt'

lines = []

def write_append(line):
    writefile = open(outfile,'a')
    writefile.write(line)
    writefile.write('\n')
    writefile.close()

with open(ifile, 'r') as infile:
    lines = infile.readlines()

random.shuffle(lines)
for line in lines:
	line = line.strip()
	print(line)
	#write_append(line)