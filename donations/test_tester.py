from django.test import TestCase
import pytest

from donations.tester import equals

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