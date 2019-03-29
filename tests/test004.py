import unittest
from time import sleep

from testee.services.selenium_service import loadWebDriver_localCHROME, take_snapshot, loadWebDriver_localFIREFOX

from selenium import webdriver
class TestFlip(unittest.TestCase):
    def test_buy_product(self):

        url = 'https://staging.gigacover.com/'
        wd = loadWebDriver_localFIREFOX()
        wd.get(url)
        x = wd.find_element_by_xpath('//a[@aqa-single-nav-link-flip]')
        x.click()
        sleep(2)
        take_snapshot(wd, '001 click flip page')

        x_list = wd.find_elements_by_xpath('//button[@aqa-list-button-get-quote-now]')
        basic = x_list[0]
        basic.click()
        sleep(2)
        take_snapshot(wd, '002 click get quote now for basic level')

        x_list = wd.find_elements_by_xpath('//div[@aqa-list-checkbox-relevant-work]')
        a_relevant_work = x_list[25]
        a_relevant_work.click()
        a_about_yourself = wd.find_element_by_id('headless-checkbox-outdoor')
        a_about_yourself.click()
        sleep(2)
        take_snapshot(wd, '003 chosen 2 checkbox')

        x2 = wd.find_element_by_xpath('//*[@aqa-single-div-show-me-my-quote]')
        x2.click()
        sleep(2)
        take_snapshot(wd, '004 after clicked button show me my quote')

        wd.quit()
