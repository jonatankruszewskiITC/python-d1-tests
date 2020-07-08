from project import find_max
import pytest
import pytest_expect


def TEST_EX01_001():
    assert find_max([4, 235, 664, 3, 2]) == 664, "Case: General. not passing"


def TEST_EX01_002():
    assert find_max([0, 3, 5, -10]) == 5, "Case: Negative number in list. Not Passing"


def TEST_EX01_003():
    assert find_max([3]) == 3, "Case: List of length 1. Not Passing"


def TEST_EX01_004():
    assert find_max(find_max([]) == None)


TEST_EX01_001()
TEST_EX01_002()
TEST_EX01_003()
# TEST_EX01_004()

