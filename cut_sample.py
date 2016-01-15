# pip install pydub
# brew install libav --with-libvorbis --with-sdl --with-theora

# This will take one input wav, cut it up and mash it back together.
# If you want different time slices, change the futureslice variable. 1000 = 1 second

# Run like this: python cut_sample.py sample.wav
# Output will be the filename you used with _sliced.wav after it.

from pydub import AudioSegment
import os
from os import walk
import random
import sys

filename = sys.argv[1]
filelist = []
randomized_list = []
outfile = filename + '_sliced.wav'

def remove_files():
	if os.path.isfile(outfile):
		os.system('rm ' + outfile) 

def cutsampleup():
	sound = AudioSegment.from_wav(filename)
	length = len(sound)
	soundslice = 0
	futureslice = 500

	
	x = 0
	# Create the first sample slice:
	#firstsample = sound[:futureslice]
	#firstsample.export("{}".format(x) + outfile, format ='wav')
	# Continue through and save the additional parts:
	
	while x < length:
		segment = sound[soundslice:soundslice + futureslice]
		filelist.append(segment)
		# This line will export all the slices as individual wavs:
		#segment.export("{}".format(x) + outfile, format ='wav')
		soundslice += futureslice
		x +=futureslice

def randomize():
	random.shuffle(filelist)
	for item in filelist:
		randomized_list.append(item)

def process_file():
	# Loop through the filelist array to get the list:
	length = len(randomized_list) # For the range, so we can iterate through the list of files.
	firstfile = randomized_list[0]

	for i in range(1, length):
		firstfile += randomized_list[i]

	firstfile.export(outfile, format ='wav')


remove_files()
cutsampleup()
randomize()
process_file()