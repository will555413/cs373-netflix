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
	temp = []
	line = next(IN)
	while True:
		if line.find(':')>-1 and random()*30 <= 1:
			temp.append(line)
			first = True
			try:
				line = next(IN)
				while (first or random()*10 <= 5) and line.find(':')<0:
					temp.append(line)
					line = next(IN)
					first = False
			except StopIteration:
				break
		else:
			try:
				line = next(IN)
				while line.find(':')<0:
					line = next(IN)
			except StopIteration:
				break
	
	for item in temp:
		OUT.write(item)

		

# ----
# main
# ----

if __name__ == "__main__" :
    input_gen(open('/u/wc6892/Documents/cs373-netflix/probe.txt', 'r', encoding = "ISO-8859-1"),
    		  open('/u/wc6892/Documents/cs373-netflix/RunNetflix.in', 'w'))