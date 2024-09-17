'''calculator Test'''
import pytest
from app.main import addition
from app.main import subtraction
from app.main import multiply
from app.main import division

def test_addition():
    '''Addition funtion'''
    assert addition(1,1)  == 2

def test_subtraction():
    '''Subtraction funtion'''
    assert subtraction(1,1)  == 0

def test_multiply():
    '''Multiply funtion'''
    assert multiply(1,1)  == 1

def test_division():
    '''Division funtion'''
    assert division(4,2)  == 2

def test_division_by_zero_exception():
    '''Division funtion testing that I get the exception divide by zero'''
    with pytest.raises(ZeroDivisionError):
        division(10,0)
    #assert division(2,0)  == 1
        