# coding: utf-8
'''
Created on 2017年9月8日

@author: zhanghui
'''
'''
test1.py 
抽取配置：用yaml文件放配置。
在config层添加配置文件config.yaml，在utils层添加file_reader.py与config.py来管理。
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.config import Config, DRIVER_PATH


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
        print result.text
    
    
    def testSearchPython(self):
        self.driver.find_element(*self.locator_searchfield).send_keys('Python')
        self.driver.find_element(*self.locator_searchbutthon).click()
        
        result = self.driver.find_element(*self.locator_searchresult)
        print result.text
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()