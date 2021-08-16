import pytest

from task1 import move_zeros
from random import choices, shuffle
from itertools import product

def test_smoke():
    assert 1+1==2

def test_basic_move_zeros():
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert all([a == b for a, b in zip(move_zeros([7, 2, 0, 1, 0]), [7, 2, 1, 0, 0])])

def fixed():
    for size in range(5):
        yield from map(list, product([0, 1, 2], repeat=size))

def cases_without_zeros():
    sizes = list(range(10)) * 2
    for size in sizes:
        yield list(choices(range(1, 10), k=size))

def cases_with_zeros():
    zeros = range(5, 10)
    notzeros = range(5)
    for zero, nonzero in product(zeros, notzeros):
        xs = choices(range(1, 10), k=nonzero) + ([0] * zero)
        shuffle(xs)
        yield xs

def test_random():
    cases = [*cases_with_zeros(), *cases_without_zeros(), *fixed()]
    shuffle(cases)
    for xs in cases:
        expected = [x for x in xs if x != 0] + [x for x in xs if x == 0]
        assert move_zeros(xs) == expected