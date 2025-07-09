import pytest

from module_1 import add

def test_add():
    assert add(9,0)==9
    assert add(10,12.3)==22.3
    assert add(10,12) == 22
    assert add(1,2) == 3
    assert add(-10.11,14.13)==pytest.approx(4.02)
