# coding:utf-8
'''
Created on 2018年3月21日

@author: zhanghui
'''
import unittest
from selenium import webdriver
import time


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.get('https://www.ciliba.org/')


    def tearDown(self):
        self.driver.quit()


    def testName(self):
        alert = self.driver.switch_to_alert()
        print (alert.text)
        alert.accept()
        time.sleep(2)
        search = self.driver.find_element_by_id('search')
        search.clear()
        search.send_keys(u'肖申克的救赎')
        
        self.driver.find_element_by_id('btnSearch').click()
        
        result = self.driver.find_element_by_xpath("//a[contains(@href,'https://www.ciliba.org/detail/')][1]")
        result.click()
        print result.text
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()