import pytest
from calculator import add, substract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(5, 5) == 10
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_substract():
    assert substract(10, 5) == 5
    assert substract(567, 560) == 7
    assert substract(20, 14) == 6
    assert substract(10, 14) == -4
    assert substract(0, 0) == 0