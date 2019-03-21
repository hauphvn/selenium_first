import unittest

from testee.services.add import add


class TestAdd(unittest.TestCase):

    def test_01(self):
        print('hello')

    def test_02(self):
        # input
        a = 1
        b = 2

        # get actual output
        result = add(a,b)

        # check expected output
        assert result == 3
