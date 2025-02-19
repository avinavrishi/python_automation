import pytest
from app import func

# @pytest.mark.smoke
# @pytest.mark.skip
# @pytest.mark.xfail
def test_FirstCase():
    print("Good Morning")
    # assert func(4) == 6
    return 0

def test_SecondCase():
    assert test_FirstCase() == 0
    print("bye")