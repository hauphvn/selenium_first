import unittest

from testee.services.selenium_service import loadWebDriver_localCHROME


class TestAdd(unittest.TestCase):

    def test_homepage(self):
        url = 'https://release.gigacover.com'
        wd = loadWebDriver_localCHROME()

        wd.get(url)
        title = wd.title
        assert title == 'Insurance for Freelancers'
