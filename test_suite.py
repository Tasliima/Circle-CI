#this is a test
from Function import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_numbers_zero():
    assert add_numbers(10, 0) == 10