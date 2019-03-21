import unittest

from testee.services.selenium_service import loadWebDriver_localCHROME


class TestAdd(unittest.TestCase):

    def test_homepage(self):
        url = 'https://release.gigacover.com'
        wd = loadWebDriver_localCHROME()

        wd.get(url)
        title = wd.title
        assert title == 'Insurance for Freelancers'

    def test_google(self):
        wd = loadWebDriver_localCHROME()
        # go to the google home page
        wd.get('http://www.google.com')

        # the page is ajax so the title is originally this:
        print(wd.title)

        # find the element that's name attribute is q (the google search box)
        inputElement = wd.find_element_by_name('q')

        # type in the search
        inputElement.send_keys('cheese!')

        # submit the form (although google automatically searches now without submitting)
        inputElement.submit()

        try:
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            WebDriverWait(wd, 10).until(EC.title_contains('cheese!'))

            # You should see 'cheese! - Google Search'
            print(wd.title)

        finally:
            wd.quit()