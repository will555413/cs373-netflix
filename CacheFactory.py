#!/usr/bin/env python3

# -------
# imports
# -------

import os
import sys

# --------------------
# Cache implementation
# --------------------
"""
Global dictionaries for user caches
Each element in ucache is a list with 5 sublists, which represent the following:
[total rating of movies in 1890-1913, number of rating in said period], [of 1913-1936], [of 1936-1959], [of 1959-1982], [of 1982-2005]]
By spliting the periods into 5 subperiods, the average rating will be more relevant in predicting rating of another movie in the same period
"""
ucache = {}

"""
Since movie titles are ordered from 1 - 17770, I just use a list to stored the information.
Each movie is indexed as (its ID - 1), for example, Dinosaur Planet will be mcache[0].
Each element in mcache is a list in following format: [year published, [sum of all ratings, count of ratings]]
"""
mcache = []


# ---------
# user_read
# ---------

def user_read (ucache, mcache, direc) :
    """
    reads all files in the directory specified; expected all files to be plain text
    direc the directory to be read

    """
    assert os.path.isdir(direc)
    assert type(ucache) == dict
    assert type(mcache) == list

    # iterate through every files in the directory
    for f in os.listdir(direc):
        # open each file in read only mode 
        mrating = open(direc+"/"+f, 'r')
        # convert the first line to int to represent to movie ID
        mid = int(mrating.readline().replace(':',''))
        # get the index of the corresponding sublist that stores the data of the movies in the corresponding era 
        index = year2index(mcache[mid-1][0])

        # if mid != 4388 and mid != 6908 and mid != 7241:
        #     continue

        # iterate through all lines in the file
        for line in mrating:
            lst = line.split(',')

            uid = int(lst[0])
            rating = int(lst[1])

            mcache[mid-1][1][0]+=rating
            mcache[mid-1][1][1]+=1

            if not uid in ucache:
                ucache[uid] = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]

            if index == -1:
                for i in range(5):
                    ucache[uid][i][0]+=rating
                    ucache[uid][i][1]+=1
            else:
                ucache[uid][index][0]+=rating
                ucache[uid][index][1]+=1

    assert len(ucache) <= 480189

# ----------
# year2index
# ----------

def year2index (year) :
    """
    helper function for user_read that returns the corresponding index for the year the movie was published
    year the integer that indicate the publish year
    """
    # if the year is not declared (NULL) in the movie_titles.txt, return -1 (invalid index)
    if year == -1:
        return -1
    # then split the period (1890-2005) into 5 subperiods
    elif year < 1913:
        return 0
    elif year < 1936:
        return 1
    elif year < 1959:
        return 2
    elif year < 1982:
        return 3
    elif year <= 2005:
        return 4

# ----------
# movie_read
# ----------

def movie_read (mcache, titles) :
    """
    reads all movie IDs and their corresponding year into the movie dictionary
    also setup each entry in the movie dictionary
    titles the file that stored the information about movie titles
    """
    assert type(mcache) == list
    # global mcache
    for line in titles:
        lst = line.split(',')
        mcache.append([-1 if lst[1] == "NULL" else int(lst[1])  ,[0.0,0.0]])
        assert int(lst[0]) == len(mcache)
    

# --------------
# cal_avg_rating
# --------------

def cal_avg_rating (cache):
    if type(cache) == dict:
        for i in cache:
            for j in range(5):
                if cache[i][j][0] != 0 and cache[i][j][1] != 0:
                    cache[i][j] = cache[i][j][0]/cache[i][j][1]
                else:
                    cache[i][j] = 0

    elif type(cache) == list:
        for i in range(len(cache)):
            if cache[i][1][0] != 0 and cache[i][1][1] != 0:
                cache[i][1] = cache[i][1][0]/cache[i][1][1]
            else:
                cache[i][1] = 0

    else:
        print("cache input not a list or dict")

# ---------
# print_lst
# ---------

def print_lst (cache):
    """
    helper function that allow me to see the data inside the cache
    cache the input cache; it will be ucache or mcache
    """
    if type(cache) == dict:
        print("user_cache")
        for i in cache:
            print("user["+str(i)+"]: "+str(cache[i]))

    elif type(cache) == list:
        print("movie_cache")
        for i in range(len(cache)):
            print("movie["+str(i+1)+"]: "+str(cache[i]))

    else:
        print("cache input not a list or dict")

# ------------
# output_cache
# ------------

def output_cache(cache, w):
    if type(cache) == dict:
        for i in cache:
            w.write(str(i)+" ")
            for j in range(5):
                w.write(str(cache[i][j])+" ")
            w.write("\n")

    elif type(cache) == list:
        for i in range(len(cache)):
            w.write(str(i+1)+" "+str(cache[i][0])+" "+str(cache[i][1])+"\n")

    else:
        print("cache input not a list or dict")

# -------------
# cache_produce
# -------------

def cache_produce (w) :
    """
    calls the cache construction functions and output the result to the file specified
    """


    """
    dictionaries for user caches
    Each element in ucache is a list with 5 sublists, which represent the following:
    [total rating of movies in 1890-1913, number of rating in said period], [of 1913-1936], [of 1936-1959], [of 1959-1982], [of 1982-2005]]
    By spliting the periods into 5 subperiods, the average rating will be more relevant in predicting rating of another movie in the same period
    """
    ucache = {}

    """
    Since movie titles are ordered from 1 - 17770, I just use a list to stored the information.
    Each movie is indexed as (its ID - 1), for example, Dinosaur Planet will be mcache[0].
    Each element in mcache is a list in following format: [year published, [sum of all ratings, count of ratings]]
    """
    mcache = []

    movie_read(mcache, open('/u/downing/cs/netflix/movie_titles.txt', 'r', encoding = "ISO-8859-1"))
    user_read(ucache, mcache, "/u/downing/cs/netflix/training_set")

    cal_avg_rating(mcache)
    cal_avg_rating(ucache)

    output_cache(ucache, open('/u/wc6892/Documents/cs373-netflix/ucache.txt', 'w'))
    output_cache(mcache, open('/u/wc6892/Documents/cs373-netflix/mcache.txt', 'w'))

# ----
# main
# ----

if __name__ == "__main__" :
    cache_produce(sys.stdout)