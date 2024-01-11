import pytest
from add import add

@pytest.mark.parametrize("a,b,expected",[
  (1,1,2),
  (3,2,5),
  (-2,-2,-4),
  (-4,4,0)
])

def test_add(a,b,expected):
  got = add(a,b)
  assert expected == got, f"{expected=}, {got=}"