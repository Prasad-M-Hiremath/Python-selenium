import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["rahul", "Shetty", "rahulshetty.com"]


@pytest.fixture(params=[("Chrome","Rahul","shetty"),("Firefox","Shetty"),("IE","SS")])
def crossBrowser(request):
    return request.param