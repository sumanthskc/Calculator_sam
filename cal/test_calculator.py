import pytest
import calculator as app
def test_add():
    assert app.add(2, 3) == 5

def test_sub():
    assert app.sub(5, 2) == 3

def test_mul():
    assert app.mul(3, 4) == 12

def test_div():
    assert app.div(10, 2) == 5
    assert app.div(10, 0) == 0
    
    