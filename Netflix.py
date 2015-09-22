#!/usr/bin/env python3

# --------------------
# Cache implementation
# --------------------
"""
Use Python Dictionary!!!!
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
# netflix_read
# ------------

def netflix_read (s) :
    """
    
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# netflix_eval
# ------------

def netflix_eval (i, j) :
    """
    
    """
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
# netflix_print
# -------------

def netflix_print (w, i, j, v) :
    """
    
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def netflix_solve (r, w) :
    """
    
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
