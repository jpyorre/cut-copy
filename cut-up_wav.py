# pip install pydub
# brew install libav --with-libvorbis --with-sdl --with-theora
# To do: Make it randomize the selections

from pydub import AudioSegment
import os
from os import walk
import random
import shutil
import tempfile

files = []
filelist = []
temp = 'temp.wav'
outfile = 'mashup.wav'

for (dirpath, dirnames, filenames) in walk('./'):
	files.extend(filenames)
	break

def process_file(filename):
	sound = AudioSegment.from_wav(filename)
	return sound

# Create an array containing all wav files in the current directory:
x = 0
for filename in files:
		if '.wav' in filename:
			x +=1
			filelist.append(filename)

file1 = filelist[0]
shutil.copy(file1, temp)

tempfile = process_file(temp) # Create a tempfile from the very first file
firstfile = tempfile[:1] # Create a 1 millisecond temp file from the tempfile. Has to be this way to have a starter file

# Loop through the filelist array to get the list:
length = len(filelist) # For the range, so we can iterate through the list of files.
for i in range(0, length):
	firstfile += process_file(filelist[i])

# Export the file as mashup.wav
firstfile.export(outfile, format='wav')

# Remove the temp file
if os.path.isfile(temp):
        os.system('rm ' + temp) 