import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_GreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])