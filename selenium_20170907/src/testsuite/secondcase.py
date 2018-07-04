# coding: utf-8
'''
Created on 2017年9月8日

@author: zhanghui
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.implicitly_wait(30)
        self.driver.get('https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn')


    def tearDown(self):
        self.driver.quit()


    def testName(self):
        '''
        #login = self.driver.find_element_by_xpath('//a[contains(@href,"mycsdn")]')
        login = self.driver.find_element_by_xpath('//*[@id="login"]/a[1]')
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(login))
            login.click()
        except:
            print 'timeout'
        '''
        self.driver.find_element_by_id('username').send_keys('zhtlforever@163.com')
        self.driver.find_element_by_id('password').send_keys('huiwenyuan011026')
        self.driver.find_element_by_class_name('logging').click()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()