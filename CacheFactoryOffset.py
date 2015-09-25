#!/usr/bin/env python3

# -------
# imports
# -------

import os
import sys

# ---------
# user_read
# ---------

def user_read (mcache, direc) :
    """
    reads all files in the directory specified; expected all files to be plain text
    direc the directory to be read

    """
    assert os.path.isdir(direc)
    assert type(mcache) == list

    ucache = {}

    trat = 0
    tcnt = 0

    # iterate through every files in the directory
    for f in os.listdir(direc):
        # open each file in read only mode 
        mrating = open(direc+"/"+f, 'r')
        # convert the first line to int to represent to movie ID
        mid = int(mrating.readline().replace(':',''))

        # iterate through all lines in the file
        for line in mrating:
            lst = line.split(',')

            uid = int(lst[0])
            rating = int(lst[1])

            mcache[mid-1][0]+=rating
            mcache[mid-1][1]+=1

            if not uid in ucache:
                ucache[uid] = [0.0,0.0]

            ucache[uid][0]+=rating
            ucache[uid][1]+=1

            trat += rating
            tcnt += 1

    assert len(ucache) <= 480189
    return (ucache, trat/tcnt)

# ----------
# movie_read
# ----------

def movie_read (titles) :
    """
    reads all movie IDs and their corresponding year into the movie dictionary
    also setup each entry in the movie dictionary
    titles the file that stored the information about movie titles
    """
    mcache = []
    for line in titles:
        lst = line.split(',')
        mcache.append([0.0,0.0])
        assert int(lst[0]) == len(mcache)
    return mcache
    

# ----------
# cal_offset
# ----------

def cal_offset (cache, avg):
    if type(cache) == dict:
        for i in cache:
            cache[i] = cache[i][0]/cache[i][1] - avg

    elif type(cache) == list:
        for i in range(len(cache)):
            cache[i] = cache[i][0]/cache[i][1] - avg

    else:
        print("cache input not a list or dict")

# ------------
# output_cache
# ------------

def output_cache(cache, w):
    w.truncate()
    if type(cache) == dict:
        for i in cache:
            w.write(str(i)+" "+str(cache[i])+"\n")

    elif type(cache) == list:
        w.write(str(cache[len(cache)-1])+"\n")
        for i in range(len(cache)-1):
            w.write(str(cache[i])+"\n")

    else:
        print("cache input not a list or dict")

# -------------
# cache_produce
# -------------

def cache_produce () :
    """
    calls the cache construction functions and output the result to the file specified
    """

    """
    list for movie
    each entry is the sum and count of all ratings received by each movie, which will be used later to calculate the user offset
    """
    mcache = movie_read(open('/u/downing/cs/netflix/movie_titles.txt', 'r', encoding = "ISO-8859-1"))

    """
    dictionaries for user caches
    each entry contain the sum and count of all ratings given by each user, which will be used later to calculate the user offset
    mean is the average of all ratings from all movies
    """
    ucache, mean = user_read(mcache, "/u/downing/cs/netflix/training_set")

    cal_offset(mcache, mean)
    cal_offset(ucache, mean)

    mcache.append(mean)

    output_cache(ucache, open('/u/wc6892/Documents/cs373-netflix/wc6892-ucacheoff.txt', 'w'))
    output_cache(mcache, open('/u/wc6892/Documents/cs373-netflix/wc6892-mcacheoff.txt', 'w'))

# ----
# main
# ----

if __name__ == "__main__" :
    cache_produce()