import unittest

from testee.services.selenium_service import loadWebDriver_localCHROME, take_snapshot


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
        take_snapshot(wd)

        # the page is ajax so the title is originally this:
        print(wd.title)

        # find the element that's name attribute is q (the google search box)
        inputElement = wd.find_element_by_name('q')

        # type in the search
        inputElement.send_keys('cheese!')
        take_snapshot(wd)

        # submit the form (although google automatically searches now without submitting)
        inputElement.submit()

        try:
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            WebDriverWait(wd, 10).until(EC.title_contains('cheese!'))
            take_snapshot(wd)

            # You should see 'cheese! - Google Search'
            print(wd.title)

        finally:
            wd.quit()

    def test_income_projection(self):
        url = 'https://release.gigacover.com/flip'
        wd = loadWebDriver_localCHROME()
        wd.get(url)

        list_levels_title = wd.find_elements_by_xpath(
            '//div[contains(@class, "box-circle") '
            'and contains(@class, "none-gutter-left") '
            'and contains(@class, "none-gutter-right")]'
            '/h2[contains(@class, "text-center")'
            ' and contains(@class, "underline")]')

        list_big_num = wd.find_elements_by_xpath(
            '//div[contains(@class, "none-gutter-right")]'
            '/h1[contains(@class, "big-num")]')

        list_start_from = wd.find_elements_by_xpath(
            '//div[contains(@class,"box-circl")'
            ' and contains(@class,"none-gutter-left")'
            ' and contains(@class, "none-gutter-right")]'
            '/p[contains(@class, "text-center")]')

        # get actual output
        OUT = lambda: None
        OUT.level1_title = list_levels_title[0].text
        OUT.level2_title = list_levels_title[1].text
        OUT.level3_title = list_levels_title[2].text

        OUT.level1_big_num = list_big_num[0].text
        OUT.level2_big_num = list_big_num[1].text
        OUT.level3_big_num = list_big_num[2].text

        OUT.level1_starting_from = list_start_from[0].text
        OUT.level2_starting_from = list_start_from[1].text
        OUT.level3_starting_from = list_start_from[2].text


        # check expected output
        assert OUT.level1_title == 'BASIC'
        assert OUT.level2_title == 'ENHANCED'
        assert OUT.level3_title == 'PREMIUM'

        assert OUT.level1_big_num == '50'
        assert OUT.level2_big_num == '100'
        assert OUT.level3_big_num == '200'

        assert OUT.level1_starting_from.find('2.26') != -1
        assert OUT.level2_starting_from.find('4.23') != -1
        assert OUT.level3_starting_from.find('7.93') != -1
