import pytest
from myapp_mutply import mutiply

@pytest.mark.parametrize('n1,n2,expected', [(0, 0, 0), (0,1,0), (2,1,2), (7,3,21), (2.3,5,11.5), ("dois",0,None), (-3,2,-6)])
def test_soma(num1,num2, expected):
    assert soma(num1,num2) == expected
