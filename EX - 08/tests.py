from project import sum_numbers


def test_function():
    assert sum_numbers(2, 4) == 6
    assert sum_numbers(3, 7) == 10
    assert sum_numbers(2, 8) == 10
    assert sum_numbers(3, 1) == 4

