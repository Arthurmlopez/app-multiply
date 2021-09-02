import pytest
from myapp_mutply import mutiply

@pytest.mark.parametrize('num1,num2,expected', [(0, 0, 0), (0,1,0), (2,1,2), (7,3,21), (2.3,5,11.5), ("dois",0,None), (-3,2,-6)])
def test_mutiply(num1,num2, expected):
    assert mutiply(num1,num2) == expected
