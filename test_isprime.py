from isPrime  import *
import pytest

def test_isprime():
    assert is_prime(7) == True
    assert is_prime(8) == False

