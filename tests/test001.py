import unittest

from testee.services.add import add


class TestAdd(unittest.TestCase):

    def test_01(self):
        print('hello')

    def test_02(self):
        # input
        INP = lambda :None
        INP.a = 1
        INP.b = 2

        # get actual output
        OUT = lambda :None
        actual_output = add(INP.a, INP.b)

        # check expected output
        assert actual_output == 3
