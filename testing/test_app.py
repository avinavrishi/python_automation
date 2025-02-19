import pytest
from app import func

# Function names should start or ends with test_ or _test
# pytest app.py
# py.test - to test all the test cases of all the test files of a folder
# py.test -v - give additional info and -v stands for verbose
# py.test -v -s give additional info with console output(-s)
# py.test -k Second -v -s - find test function or file which contain second keyword and test them.

# @pytest.mark.smoke
def test_FirstAnswer():
    assert func(5) == 6, "This test case failed correct answer is 5."

def test_SecondAnswer():
    print(func(5))
    
