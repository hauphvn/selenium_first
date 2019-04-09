#!/usr/bin/env python3

import unittest
from time import sleep
from selenium import webdriver
from testee.services import selenium_service as ss
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class TestFlip(unittest.TestCase):
    def test_buy_product(self):

        url = 'https://staging.gigacover.com/'
        # wd = loadWebDriver_localFIREFOX(browserName)
        wd = ss.loadWebDriver_seleniumGrid('chrome')
        wd.get(url)
        ss.take_snapshot(wd, wd.name,'home-page')

        x = wd.find_element_by_css_selector('#gigacover-landing > div:nth-child(1) > header > nav > div.col-xs-10.text-right > ul > li:nth-child(1) > a')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'after click flip page')

        x = wd.find_element_by_css_selector('#gigacover-landing > div.flip > section:nth-child(5) > div > div.col-xs-12.md-gutter-bottom.quote-plan-box > div:nth-child(1) > div > div.row.text-center > button > span')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'after click button get quote now basic')

        x = wd.find_element_by_css_selector('#page-top > div.MuiModal-root-16.MuiDialog-root-29.QuoteFormModal-rootDialog-26 > div.MuiDialog-container-32.MuiDialog-scrollPaper-30 > div > div.MuiDialogContent-root-172.QuoteFormModal-dialogContent-28 > div > div:nth-child(4) > div:nth-child(27) > label > span.MuiTypography-root-121.MuiTypography-body2-129.MuiFormControlLabel-label-228.QuoteFormModal-label-23')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'check checkbox in  relevant work')

        x = wd.find_element_by_css_selector('#page-top > div.MuiModal-root-16.MuiDialog-root-29.QuoteFormModal-rootDialog-26 > div.MuiDialog-container-32.MuiDialog-scrollPaper-30 > div > div.MuiDialogContent-root-172.QuoteFormModal-dialogContent-28 > div > div:nth-child(7) > div.col-xs-12.col-sm-8.custom-xs > label:nth-child(1) > span.MuiTypography-root-121.MuiTypography-body2-129.MuiFormControlLabel-label-228.QuoteFormModal-label-23')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'check checkbox in  more about yourself')

        x = wd.find_element_by_xpath('//*[@aqa-single-div-show-me-my-quote]')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'after click button show me my quote')

        x = wd.find_element_by_css_selector('#gigacover-landing > div.income-quote > div > div.row.letter > div:nth-child(8) > div:nth-child(7) > div.col-xs-2 > div > div > button')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'choose payment option')

        x = wd.find_element_by_css_selector('#headless-checkbox-daily_benefit')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'click checkbox term')

        x = wd.find_element_by_css_selector("#headless-proceed-info-button")
        y = wd.find_element_by_xpath('//a[*="Terms of use"]')
        wd.execute_script('arguments[0].scrollIntoView(true);', y)
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'after click button proceed')

        firstname = wd.find_element_by_css_selector('#headless-first-name')
        firstname.send_keys('hauphvn')

        lastname = wd.find_element_by_css_selector('#headless-last-name')
        lastname.send_keys('hcmus123')

        nric = wd.find_element_by_css_selector('#headless-nric')
        nric.send_keys('S0726624C')

        postalcode = wd.find_element_by_css_selector('#headless-postalcode')
        postalcode.send_keys('088278')

        email = wd.find_element_by_css_selector('#headless-email')
        email.send_keys('hauphvn123@gmail.com')

        mobile = wd.find_element_by_css_selector('#headless-mobile')
        mobile.send_keys('65678634')
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'fill in information')

        x = wd.find_element_by_css_selector('#headless-checkbox-confirm-info')
        x.click()
        x = wd.find_element_by_css_selector('#headless-checkbox-required')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'check confirm and required')

        x = wd.find_element_by_css_selector('#headless-proceed-checkout-button')
        x.click()
        sleep(3)
        ss.take_snapshot(wd, wd.name, 'after click checkout now')

        x = wd.find_element_by_css_selector('#headless-proceed-payment-button')
        x.click()

        sleep(3)
        ss.take_snapshot(wd, wd.name, 'click pay by card')

        x = wd.find_element_by_xpath("//iframe[@name='stripe_checkout_app']")
        wd.switch_to.frame(x)

        cardNumber = wd.find_element_by_xpath("//input[@placeholder='Card number']")
        cardNumber.send_keys('4242424242424242')

        mmyy = wd.find_element_by_xpath("//input[@placeholder='MM / YY']")
        mmyy.send_keys('12/23')

        cvc = wd.find_element_by_xpath("//input[@placeholder='CVC']")
        cvc.send_keys('302')

        zipcode = wd.find_element_by_xpath("//input[@placeholder='ZIP Code']")
        zipcode.send_keys('349245')

        pay_btn = wd.find_element_by_xpath("//button[@type='submit']")
        pay_btn.click()

        ss.take_snapshot(wd, wd.name, 'after click pay')
        wd.switch_to.default_content()

        sleep(15)
        ss.take_snapshot(wd, wd.name, 'thank you page')
        wd.quit()

