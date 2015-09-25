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

    def test_user_read_4 (self) :
        s    = StringIO("777 -888\n-777 888\n99999999 -99999999")
        Dict = user_cache_read(s)
        self.assertEqual(Dict[777],      -888)
        self.assertEqual(Dict[-777],     888)
        self.assertEqual(Dict[99999999], -99999999)

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

    def test_mov_read_4 (self) :
        s   = StringIO("99999999\n-99999999\n0.0000001\n-0.0000001")
        lst = mov_cache_read(s)
        self.assertEqual(lst[0], 99999999)
        self.assertEqual(lst[1], -99999999)
        self.assertEqual(lst[2], 0.0000001)
        self.assertEqual(lst[3], -0.0000001)

    # -------------
    # netflix_solve
    # -------------

    def test_solve_1 (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n2488120\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.78\n3.38\n3.69\n4.8\nRMSE: 0.49\n")

    def test_solve_2 (self) :
        r = StringIO("10000:\n200206\n523108\n10001:\n262828\n2609496\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10000:\n3.7\n3.56\n10001:\n3.49\n4.39\nRMSE: 0.76\n")

    def test_solve_3 (self) :
        r = StringIO("1372:\n2449527\n1975483\n13731:\n1671304\n13746:\n982771\n2101154\n13819:\n129921\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1372:\n3.7\n2.82\n13731:\n2.68\n13746:\n3.13\n3.11\n13819:\n3.8\nRMSE: 0.87\n")

    def test_solve_4 (self) :
        r = StringIO("15724:\n1923980\n1573:\n441153\n2041252\n1005679\n1361562\n15734:\n1458083\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "15724:\n3.21\n1573:\n3.25\n3.16\n3.37\n3.38\n15734:\n2.61\nRMSE: 1.04\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()