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

from Netflix import collatz_read # import methods to be tested

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "5000 2\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  5000)
        self.assertEqual(j, 2)

    def test_read_3 (self) :
        s    = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    def test_read_4 (self) :
        s    = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  900)
        self.assertEqual(j, 1000)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1 (self) :
        v = cycle_length(1)
        self.assertEqual(v, 1)

    def test_cycle_length_2 (self) :
        v = cycle_length(10)
        self.assertEqual(v, 7)

    def test_cycle_length_3 (self) :
        v = cycle_length(200)
        self.assertEqual(v, 27)

    def test_cycle_length_4 (self) :
        v = cycle_length(100000)
        self.assertEqual(v, 129)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 5000, 2, 238)
        self.assertEqual(w.getvalue(), "5000 2 238\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("5000 2\n200 200\n1 1\n17 827067\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "5000 2 238\n200 200 27\n1 1 1\n17 827067 509\n")

    def test_solve_3 (self) :
        r = StringIO("2178 166660\n43275 86861\n8498 25440\n1 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "2178 166660 383\n43275 86861 351\n8498 25440 282\n1 999999 525\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()