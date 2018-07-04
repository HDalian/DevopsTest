# coding: utf-8
'''
Created on 2017年9月7日

@author: zhanghui
'''
import unittest
from selenium import webdriver

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.get('http://www.baidu.com')


    def tearDown(self):
        self.driver.quit()


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()