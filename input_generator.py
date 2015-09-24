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
	first = False
	for line in IN:
		if line.replace('\n', '').endswith(':') and int(random()*100) == 1:
			temp.append(line)
			first = True
		elif int(random()*1000) == 500 or first:
			temp.append(line)
			first = False

	begin = False
	for item in temp:
		if begin:
			OUT.write(item)
			continue
		if item.replace('\n', '').endswith(':'):
			begin = True

		

# ----
# main
# ----

if __name__ == "__main__" :
    input_gen(open('/u/wc6892/Documents/cs373-netflix/probe.txt', 'r', encoding = "ISO-8859-1"),
    		  open('/u/wc6892/Documents/cs373-netflix/RunNetflix.in', 'w'))