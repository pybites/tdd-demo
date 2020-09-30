import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.fixture
def init_operations(calc):
    calc.multiply(8, 2)
    calc.divide(8, 2)
    calc.subtract(8, 2)


def test_empty_calculator_instance(calc):
    assert calc.operations == {}


def test_add(calc):
    assert calc.add(2, 2) == 4
    assert calc.operations == {
        (2, 2, '+'): 4}


def test_subtract(calc):
    assert calc.subtract(2, 2) == 0
    assert calc.operations == {
        (2, 2, '-'): 0}



def test_multiply(calc):
    assert calc.multiply(2, 2) == 4
    assert calc.operations == {
        (2, 2, '*'): 4}


def test_divide(calc):
    assert calc.divide(8, 2) == 4
    assert calc.operations == {
        (8, 2, '/'): 4}


def test_cache_multiple_operations(calc, init_operations):
    assert calc.operations == {
        (8, 2, '*'): 16,
        (8, 2, '/'): 4,
        (8, 2, '-'): 6,
    }


def test_print_operations(calc, capfd, init_operations):
    expected = (
        "8 * 2 = 16\n"
        "8 / 2 = 4\n"
        "8 - 2 = 6\n")
    calc.print_operations()
    actual = capfd.readouterr()[0]
    assert actual == expected


def test_two_additions_second_one_uses_cache(calc):
    calc.add(8, 2)
    calc.add(8, 2)
    assert calc.operations == {
        (8, 2, '+'): 10}
