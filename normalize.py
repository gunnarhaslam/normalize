#!/usr/bin/env python
'''
gunnar haslam - gunnar.haslam@gmail,com
5 december 2016

normalize.py - normalize 16/24-bit wav files in current directory 
	       24-bit files automatically converted to 16-bit

call from bash shell as:
	$ python normalize.py

'convertBitDepth' function adapted from warren weckesser - 
		https://gist.github.com/WarrenWeckesser/7461781#file-wavio-py-L20


Version 1.0

'''

import numpy as np
from scipy.io import wavfile
import os
import wave

# OPTIONS
#
# backup - if enabled, saves backup file under name '_unprocessed_<filename>'
backup = 1

def convertBitDepth(filename):
    # open file and read data
    wav = wave.open(filename)
    fs = wav.getframerate()
    nchannels = wav.getnchannels()
    width = wav.getsampwidth()
    nframes = wav.getnframes()
    data = wav.readframes(nframes)
    nsamples = len(data) / (width * nchannels)
    wav.close()
    if width == 3:
	# 24 bit 
        a = np.empty((nsamples, nchannels, 4), dtype=np.uint8)
        raw_bytes = np.fromstring(data, dtype=np.uint8)
        a[:, :, :width] = raw_bytes.reshape(-1, nchannels, width)
        a[:, :, width:] = (a[:, :, width - 1:width] >> 7) * 255
        result = a.view('<i4').reshape(a.shape[:-1])
	quantization = (2.**31)
    else:
        dt_char = 'u' if width == 1 else 'i'
        a = np.fromstring(data, dtype='<%s%d' % (dt_char, width))
        result = a.reshape(-1, nchannels)
	quantization = (2.**15)
    return fs, result, quantization

################################################

if __name__=='__main__':

    # build list of audio files in directory
    pwd = os.getcwd()
    ls = os.listdir(pwd)
    filelist = []
    for filename in ls:
       if filename.endswith('wav'):
           filelist.append(filename)

    # load each file and normalize
    for track in filelist:
        
	print 'Normalizing ', track, '...\n'
        fs, signal, quantization = convertBitDepth(track)

        # int to float and normalize
        signal = signal / quantization
        norm = np.amax(signal)
        sigNorm = 0.99*(signal / norm)

        # back to int
	requant = (2.**15)
        sigNorm = sigNorm * requant
        sigNorm = np.asarray(sigNorm, dtype = np.int16)

	if backup:
            # rename original
	    prefix = '_unprocessed_'
	    oldName = prefix + track
	    os.rename(track,oldName)
	else:
	    os.remove(track)

        # write
        wavfile.write(track,fs,sigNorm)


