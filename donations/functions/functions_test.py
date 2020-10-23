#from django.test import TestCase
import pytest

from functions import equals, sortByAlphabetical, calculateTotal

# Create your tests here.
class TestEquals(object):
    def test_equals(self):
        actual = equals(1, 1)
        expected = True
        assert actual == expected
    def test_notEquals(self):
        actual = equals(1, 2)
        expected = False
        assert actual == expected
class TestSorted(object):
    def test_sorted(self):
        actual = sortByAlphabetical(["c", "b", "a"])
        expected = ["a", "b", "c"]
        assert actual == expected

class TestCalculateTotal(object):
    def test_calculateTotal(self):
        actual = calculateTotal([1, 2, 3])
        expected = 6
        assert actual == expected
