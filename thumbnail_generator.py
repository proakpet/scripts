#!/usr/bin/env python3

from concurrent import futures
import argparse
import logging
import os
import sys

import PIL
import PIL.Image

from tqdm import tqdm

def process_options():

	kwargs = {
		'format' : '[%(levelname)s] %(message)s'
	}

	parser = argparse.ArgumentParser(
		description = 'Thumbnail generator',
		fromfile_prefix_chars='@'

	)
	parser.add_argument('--debug', action='store_true')
	parser.add_argument('-v', '--verbose', action='store_true')
	parser.add_argument('-q', '--quiet', action='store_true')

	options = parser.parse_args()

	if options.debug:
		kwargs['level'] = logging.DEBUG
	elif options.verbose:
		kwargs['level'] = logging.INFO
	elif options.quite:
		kwargs['level'] = logging.ERROR
	else:
		kwargs['level'] = logging.WARN

	logging.basicConfig(*kwargs)

	return options

def process_file(root, basename):
	"""Generates a thumbnail of the given image."""
	# Open the image that we need to process
	filename = f'{root}/{basename}'
	image = PIL.Image.open(filename)

	# Generate the thumbnail
	size = (128, 128)
	image.thumbnail(size)

	# Store the thumbnail in the thumbnails folder
	new_name = f'thumbnails/{basename}'
	image.save(new_name, "JPEG")
	return new_name


def progress_bar(files):
	return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)


def main():

	process_options()

	# Create the thumbnails directory
	if not os.path.exist('thumbnails'):
		os.mkdir('thumbnails')

	#executor = futures.ProcessPoolExecutor()
	executor = futures.ThreadPoolExecutor()
	for root, _, files in os.walk('images'):
		for basename in progress_bar(files):
			if not basename.endswith('.jpg'):
				continue
			executor.submit(process_file, root,basename)
	print('Waiting for all threads to finish.')
	executor.shutdown()
	return 0


if __name__ == '__main__':
	sys.exit(main())
