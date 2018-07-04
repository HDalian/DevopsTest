# coding: utf-8
'''
Created on 2017年9月8日

@author: zhanghui
'''
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')


    def tearDown(self):
        self.driver.quit()


    def testSearchOne(self):
        self.search_field = self.driver.find_element_by_id('kw')
        self.search_field.send_keys('selenium')
        self.search_field.submit()      
        
        search_result = self.driver.find_element_by_xpath('//div[contains(@class, "result")]/h3/a') 
        print search_result.text
        
    def testSearchAnother(self):
        self.search_field = self.driver.find_element_by_id('kw')
        self.search_field.send_keys(u'selenium 灰蓝')
        self.search_field.submit()
        
        search_result = self.driver.find_element_by_xpath('//*[@id="1"]/h3/a')
        print search_result.text
        search_result.click()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()