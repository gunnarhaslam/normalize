# normalize

normalize is a Python script for managing files for use with the Pioneer CDJ line. Running the script from the command line searches through the current directory for .wav files, converts 24-bit files to 16-bit, and normalizes all signals.

## Background

As a DJ, I have been using Pioneer CDJs for a long time, and have developed scripts over the years to help make my preparations for gigs as smooth as possible. *normalize.py* is one of these scripts -- more will be folded into it over the coming months.

While newer CDJ models allow 96kHz and 24-bit audio, many older models do not. 16-bit files are perfecly adequate for playback on most systems, and certainly preferable to the hassle of files not working because a venue does not have the latest hardware updates. 

Additionally, many DJs play records that they rip at home out at clubs. I typically rip my records around -6 dB to avoid any distortion problems, but in a club environment this can be too soft, forcing the DJ to rely too heavily on the mixer's (often poor) pre-amps. Normalized signals remove some of this hassle.

## Installation

Download the normalize.py script -- that's it! Requires no special libraries outside those included with most typical Python distributions.

## Usage

From the command line run:

> `$ python normalize.py`

All .wav files in the current directory will be converted to 16-bit and normalized. By default, all files will be backed up and saved with the prefix '\_unprocessed\_' (this may be turned off with an option in the script).

## Forthcoming

Version 2 will include support for AIFFs and propagation of metadata to processed files. Additionally, a basic record-ripping utility that reduces clicks and pops from static, dust, and gouges is being developed.
