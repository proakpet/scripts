#!/bin/bash

#usage example:
# >basename index.HTM .HTM
# index

for file in *.HTM; do
	name=$(basename "$file" .HTM)
	echo mv "$file" "$name.html"
done