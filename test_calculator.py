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
    
def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(1, 1) == 1
    assert multiply(2, 1) == 2
    assert multiply(8, 4) == 32
    assert multiply(0, 0) == 0

def test_divide():
    assert divide(10, 5) == 2
    assert divide(1, 1) == 1
    assert divide(2, 1) == 2
    assert divide(8, 4) == 2
    assert divide(5, 5) == 1