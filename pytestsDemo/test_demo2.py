import pytest


@pytest.mark.smoke
#@pytest.mark.skip
def test_firdtProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed strig do not match"


def test_SecodCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"



