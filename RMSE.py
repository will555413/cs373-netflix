#!/usr/bin/env python3

# ------
# import
# ------

from numpy import mean, sqrt, square, subtract

# ----
# RMSE
# ----

def RMSE (lst1, lst2) :
	return sqrt(mean(square(subtract(lst1, lst2))))

# ---------
# listifier
# ---------

def listifier (f) :
	lst = []
	for line in f:
		if line.find(':')==-1:
			lst.append(float(line))
	return lst

# ----
# main
# ----

if __name__ == "__main__" :
    print(str(RMSE(listifier(open('/u/wc6892/Documents/cs373-netflix/probe_actual.txt', 'r', encoding = "ISO-8859-1")), listifier(open('/u/wc6892/Documents/cs373-netflix/probe.out', 'r')))))