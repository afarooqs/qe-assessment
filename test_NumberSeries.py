from NumberSeries import NumberSeries
import pytest

def test_findFirstAndLast_unique_number_positive():
    num = NumberSeries(None)
    expected = (0, 0)
    result = num.findFirstAndLast([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 1)
    assert result == expected

def test_findFirstAndLast_recurring_number_positive():
    num = NumberSeries(None)
    expected = (1, 4)
    result = num.findFirstAndLast([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2)
    assert result == expected

def test_findFirstAndLast_last_number_positive():
    num = NumberSeries(None)
    expected = (2, 2)
    result = num.findFirstAndLast([1, 7, 8], 8)
    assert result == expected

def test_findFirstAndLast_one_number_array_positive():
    num = NumberSeries(None)
    expected = (0, 0)
    result = num.findFirstAndLast([1], 1)
    assert result == expected

def test_findFirstAndLast_number_not_found_negative():
    num = NumberSeries(None)
    expected = (-1, -1)
    result = num.findFirstAndLast([1, 2, 3, 4, 5], 8)
    assert result == expected

def test_findFirstAndLast_string_input_negative():
    num = NumberSeries(None)
    expected = (-1, -1)
    result = num.findFirstAndLast([1, 2, 3, 4, 5], "this is a string")
    assert result == expected

def test_findFirstAndLast_none_input_negative():
    num = NumberSeries(None)
    expected = (-1, -1)
    result = num.findFirstAndLast([1, 2, 3, 4, 5], None)
    assert result == expected

# This test case fails because True is interpreted as 1.
def test_findFirstAndLast_boolean_input_negative():
    num = NumberSeries(None)
    expected = (-1, -1)
    result = num.findFirstAndLast([1, 2, 3, 4, 5], True)
    assert result == expected

def test_findFirstAndLast__negative():
    num = NumberSeries(None)
    expected = (-1, -1)
    result = num.findFirstAndLast([1, 2, 3, 4, 5], 8)
    assert result == expected

# def test_findFirstAndLast_number_not_found_negative():
#     num = NumberSeries(None)
#     expected = (-1, -1)
#     result = num.findFirstAndLast([1, 2, 3, 4, 5], 8)
#     assert result == expected
#
# def test_findFirstAndLast_number_not_found_negative():
#     num = NumberSeries(None)
#     expected = (-1, -1)
#     result = num.findFirstAndLast([1, 2, 3, 4, 5], 8)
#     assert result == expected
#
#
