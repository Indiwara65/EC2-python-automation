import pytest

from module_3 import mult

def test_mult():
    assert mult(9,0)==0
    assert mult(10,12.3)==pytest.approx(123, rel=1e-5)
    assert mult(-10.11,14.13)==pytest.approx(-142.8543, rel=1e-5)