'''calculator Test'''
from app.main import addition
from app.main import subtraction


def test_addition():
    '''Addition funtion'''
    assert addition(1,1)  == 2

def test_subtraction():
    '''Subtraction funtion'''
    assert subtraction(1,1)  == 0