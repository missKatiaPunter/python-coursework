import pytest

from task5 import mystery_num

def test_mystery_num():
    assert mystery_num(300) == 2
    assert mystery_num(6996) == 4

@pytest.mark.parametrize("number, expected", [(666, 3), (90783, 4), (123457, 0), (81234, 2), (89282350306, 8), (3479283469, 5)])
def test_add_more(number, expected):
    result = mystery_num(number)
    assert result == expected