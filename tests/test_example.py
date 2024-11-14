from src.test import *


def test_addition():
    assert addition(2, 3) == 5
    assert addition(2, 4) == 6
    assert addition(1, 1) == 2
    assert addition(-1, 5) == 4
    assert addition(6, 7) == 13
