# coding: utf-8
'''
Created on 2017年9月8日

@author: zhanghui
'''
'''
test2.py 
添加log
在utils层添加log.py
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH

from utils.log import logger


class Test(unittest.TestCase):
    driver_path = DRIVER_PATH + '/geckodriver'
    url = Config().get('URL')
    locator_searchfield = (By.ID, 'kw')
    locator_searchbutthon = (By.ID, 'su')
    locator_searchresult = (By.XPATH, '//div[contains(@class,"result")]/h3/a')
    

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=self.driver_path)
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)
        

    def tearDown(self):
        self.driver.quit()


    def testSearchSelenium(self):
        self.driver.find_element(*self.locator_searchfield).send_keys('Selenium')
        self.driver.find_element(*self.locator_searchbutthon).click()
        
        result = self.driver.find_element(*self.locator_searchresult)
        logger.info(result.text)
    
    
    def testSearchPython(self):
        self.driver.find_element(*self.locator_searchfield).send_keys('Python')
        self.driver.find_element(*self.locator_searchbutthon).click()
        
        result = self.driver.find_element(*self.locator_searchresult)
        logger.info(result.text)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()