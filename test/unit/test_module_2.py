import pytest

from module_2 import sub

def test_sub():
    assert sub(9,0)==9
    assert sub(10,12.3)==pytest.approx(-2.3, rel=1e-5)
    assert sub(-10.11,14.13)==pytest.approx(-24.24, rel=1e-5)