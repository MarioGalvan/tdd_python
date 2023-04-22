from fibonnaci import *
import pytest

def test_make_fibonnaci():
    def test_make_fibonnaci_0():
        assert make_fibonnaci(0) == []


def test_make_fibonnaci_1():
    assert make_fibonnaci(1) == [0]


def test_make_fibonnaci_2():
    assert make_fibonnaci(2) == [0, 1]


def test_make_fibonnaci_10():
    assert make_fibonnaci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

