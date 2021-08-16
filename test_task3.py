import pytest

from task3 import bmi

def test_bmi():
    actual = bmi([74, 74, 72, 72, 73, 69, 69, 71, 76, 71],[180, 215, 210, 210, 188, 176, 209, 200,189,190])
    expected = [23.11, 27.6, 28.48, 28.48, 24.8, 25.99, 30.86, 27.89, 23.01, 26.5]
    assert actual == expected