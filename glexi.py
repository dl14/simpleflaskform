# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def scrape_definition(searchword):
    f = open('def.txt', 'w')
    print "INSIDE GLEXI"
    self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    self.driver.implicitly_wait(30)
    self.base_url = "http://www.gujaratilexicon.com/"
    self.verificationErrors = []
    self.accept_next_alert = True

    driver = self.driver
    driver.get(self.base_url + "/")
    Select(driver.find_element_by_id("selectdictionary")).select_by_visible_text("Gujarati - English")
    driver.find_element_by_id("sbtext").clear()
    driver.find_element_by_id("sbtext").send_keys(searchWord)
    driver.find_element_by_id("sbsubmit").click()

    time.sleep(2)

    htmlGL = driver.page_source
    soupGL = BeautifulSoup(htmlGL, "html.parser")
    print "Lexicon: "
    for meaning in soupGL.find_all("div", class_="meaning"):
        f.write(meaning.text)
        print meaning.text

    driver.get("http://www.shabdkosh.com/gu/")
    driver.find_element_by_id("e").clear()
    driver.find_element_by_id("e").send_keys(searchWord)
    driver.find_element_by_xpath("//button[@type='submit']").click()

    time.sleep(2)

    htmlSK = driver.page_source
    soupSK = BeautifulSoup(htmlSK, "html.parser")

    print "Shabdakosh: "
    for meaning in soupSK.find_all("a", class_="l"):
        if "%" in meaning.get('href'):
            break
        f.write(meaning.text)
        print meaning.text

    driver.get("https://www.translate.com/")
    driver.find_element_by_id("detect_button").click()
    time.sleep(2)
    driver.find_element_by_id("source_text").clear()
    time.sleep(2)
    driver.find_element_by_id("source_text").send_keys(searchWord)
    time.sleep(2)
    driver.find_element_by_id("translate_button").click()
    time.sleep(2)

    htmlT = driver.page_source
    soupT = BeautifulSoup(htmlT, "html.parser")

    print "Google Translate: "
    for meaning in soupT.find_all("div", {"id": "translation_text"}):
        f.write(meaning.text)
        print meaning.text

    f.close()
    '''
   driver.get("http://www.bhagvadgomandal.com/")
   driver.find_element_by_id("TypePad").clear()
   driver.find_element_by_id("TypePad").send_keys(searchWord)
   driver.find_element_by_xpath("//div[@id='conatiner']/div[3]/div/form/table/tbody/tr/td/table/tbody/tr/td[3]/a/img").click()

   time.sleep(2)

   htmlBG = driver.page_source
   soupBG = BeautifulSoup(htmlBG, "html.parser")

   for meaning in soupBG.find_all("a", class_="l"):
       print meaning.text
   '''

#if __name__ == "__main__":
    #scrape_definition(u"દેવ")
