#!/usr/bin/env python3

# ------
# import
# ------

from random import random

# ---------
# input_gen
# ---------

def input_gen(IN, OUT):
	"""
	reads the probe.txt provided, which has roughly 1.5 million entries
	print out a subset of the probe.txt, with 1000-2000 entries
	IN the input file
	OUT the output file
	"""
	first = False
	for line in IN:
		if line.replace('\n', '').endswith(':') and int(random()*100) == 1:
			OUT.write(line)
			first = True
		elif int(random()*1000) == 500 or first:
			OUT.write(line)
			first = False

# ----
# main
# ----

if __name__ == "__main__" :
    input_gen(open('/u/wc6892/Documents/cs373-netflix/probe.txt', 'r', encoding = "ISO-8859-1"),
    		  open('/u/wc6892/Documents/cs373-netflix/RunNetflix.in', 'w'))