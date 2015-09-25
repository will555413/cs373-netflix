#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import user_cache_read, mov_cache_read, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ---------------
    # user_cache_read
    # ---------------

    def test_user_read_1 (self) :
        s    = StringIO("1 0.1\n2 -0.1\n50 5")
        Dict = user_cache_read(s)
        self.assertEqual(Dict[1],  0.1)
        self.assertEqual(Dict[2],  -0.1)
        self.assertEqual(Dict[50], 5)

    def test_user_read_2 (self) :
        s    = StringIO("10 20\n-1 -500\n5000 0.00005")
        Dict = user_cache_read(s)
        self.assertEqual(Dict[10],   20)
        self.assertEqual(Dict[-1],   -500)
        self.assertEqual(Dict[5000], 0.00005)

    def test_user_read_3 (self) :
        s    = StringIO("0 0.001\n-50 50\n50 -50\n5 5.5555")
        Dict = user_cache_read(s)
        self.assertEqual(Dict[0],   0.001)
        self.assertEqual(Dict[-50], 50)
        self.assertEqual(Dict[50],  -50)
        self.assertEqual(Dict[5],   5.5555)

    # --------------
    # mov_cache_read
    # --------------

    def test_mov_read_1 (self) :
        s   = StringIO("10\n0.5\n0.1\n-0.5\n-0.1")
        lst = mov_cache_read(s)
        self.assertEqual(lst[0], 10)
        self.assertEqual(lst[1], 0.5)
        self.assertEqual(lst[2], 0.1)
        self.assertEqual(lst[3], -0.5)
        self.assertEqual(lst[4], -0.1)

    def test_mov_read_2 (self) :
        s   = StringIO("-10\n1000\n-1000\n0.000001\n-0.000001")
        lst = mov_cache_read(s)
        self.assertEqual(lst[0], -10)
        self.assertEqual(lst[1], 1000)
        self.assertEqual(lst[2], -1000)
        self.assertEqual(lst[3], 0.000001)
        self.assertEqual(lst[4], -0.000001)

    def test_mov_read_3 (self) :
        s   = StringIO("-0.00001\n88888\n-88888\n7.77777\n-7.77777")
        lst = mov_cache_read(s)
        self.assertEqual(lst[0], -0.00001)
        self.assertEqual(lst[1], 88888)
        self.assertEqual(lst[2], -88888)
        self.assertEqual(lst[3], 7.77777)
        self.assertEqual(lst[4], -7.77777)

    # -------------
    # netflix_solve
    # -------------

    def test_solve_1 (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n2488120\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.78\n3.38\n3.69\n4.8\n")

    def test_solve_2 (self) :
        r = StringIO("10000:\n200206\n523108\n10001:\n262828\n2609496\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10000:\n3.7\n3.56\n10001:\n3.49\n4.39\n")

    def test_solve_3 (self) :
        r = StringIO("11895:\n568614\n2502587\n11896:\n911967\n2176297\n664527\n11897:\n73119\n1204080\n897013\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "11895:\n3.64\n3.55\n11896:\n3.76\n3.31\n3.52\n11897:\n3.12\n2.82\n2.15\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()