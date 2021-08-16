import pytest

from task4 import miss_nums_finder

def test_bmi_one_missing():
    list_to_test = [2, 3, 1, 9, 4, 5, 6, 10, 7]
    assert miss_nums_finder(list_to_test) == [8]

def test_bmi():
    list_to_test = [7, 1, 12, 9, 11, 14, 13, 6, 10, 5]
    assert miss_nums_finder(list_to_test) == [2, 3, 4, 8]