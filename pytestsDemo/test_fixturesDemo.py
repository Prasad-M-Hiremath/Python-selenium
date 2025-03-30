import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixturesDemo(self):
        print("I will execute steps fixture demo method")


    def test_fixturesDemo1(self):
        print("I will execute steps fixture demo1 method")


    def test_fixturesDemo2(self):
        print("I will execute steps fixture demo2 method")


    def test_fixturesDemo3(self):
        print("I will execute steps fixture demo3 method")
