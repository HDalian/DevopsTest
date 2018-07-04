# coding: utf-8
'''
Created on 2017年9月8日

@author: zhanghui
'''
# test0.py first unittest case
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    firefox_path = '/usr/local/bin/geckodriver'
    url = 'http://www.baidu.com'
    locator_searchfield = (By.ID, 'kw')
    locator_searchbutthon = (By.ID, 'su')
    locator_searchresult = (By.XPATH, '//div[contains(@class,"result")]/h3/a')
    

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=self.firefox_path)
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)
        

    def tearDown(self):
        self.driver.quit()


    def testSearchSelenium(self):
        self.driver.find_element(*self.locator_searchfield).send_keys('Selenium')
        self.driver.find_element(*self.locator_searchbutthon).click()
        
        result = self.driver.find_element(*self.locator_searchresult)
        print result.text
    
    
    def testSearchPython(self):
        self.driver.find_element(*self.locator_searchfield).send_keys('Python')
        self.driver.find_element(*self.locator_searchbutthon).click()
        
        result = self.driver.find_element(*self.locator_searchresult)
        print result.text
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()