import pytest
from unittest import TestCase
from SOM.som import BASE_URL
from nose.tools import assert_equal


class TestSOM(TestCase):

    def test_BASE_URL(self):

        assert_equal(BASE_URL, 'https://www.boxofficemojo.com')