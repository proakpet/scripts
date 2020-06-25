#!/usr/bin/env3 python3

"""
Use the Python Imaging Library to do the following to a batch of images:
Open an image
Rotate an image
Resize an image
Save an image in a specific format in a separate directory"""
from PIL import Image
import os, glob

for file in glob.glob("images/ic_*"):
	im = Image.open(file).convert('RGB')
	im.rotate(270).resize(128, 128).save("/opt/icons"+file[7:], "JPEG")