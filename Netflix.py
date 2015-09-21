#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# Global Cache
# ------------
"""
declare and initialize a global cache that would stored the cycle length of the corresponding indexed
for example, value stored at index 10 would 7 since cycle_length of 10 is 7
"""
cache = []
# manually added cycle length of 0, which is indexed at 0, as -1 (garbage value)
cache.append(-1)
# manually added cycle length of 1, which is indexed at 1, as 1
cache.append(1)
# add cycle length placeholders into the cache, starting from 2 since 0 and 1 have been added
for idx in range(2, 1000000):
    cache.append(0)

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    assert i>0 and i<=1000000
    assert j>0 and j<=1000000

    b = j if j>i else i
    a = i if b == j else j
    a = b//2 if b//2>a else a

    max_count = -1
    for num in range(a, b+1):
        count = cycle_length(num)
        if count > max_count:
            max_count = count

    assert max_count > 0
    return max_count

# ------------
# cycle_length
# ------------

def cycle_length (num):
    """
    returns the cycle length of num
    if cache have stored a valid value, return it
    if not, get the next number in sequence and call itself recursively
    at each recursion, if num is a storable number (depends on size of cache), stored the value of return by the recursive call
    """
    global cache
    if num < len(cache) and num > -1 and cache[num] > 0:
        return cache[num]
    elif num % 2 == 1:
        next_num = num + (num // 2) + 1
        if num < len(cache) and num > -1:
            cache[num] = 2 + cycle_length(next_num)
            return cache[num]
        else:
            return 2 + cycle_length(next_num)
    else:
        next_num = num // 2
        if num < len(cache) and num > -1:
            cache[num] = 1 + cycle_length(next_num)
            return cache[num]
        else:
            return 1 + cycle_length(next_num)

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
