# coding: utf-8
'''
Created on 2017年9月8日

@author: zhanghui
'''
'''
test5.py 
将测试报告发送email
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner

from utils import sendmail


class Test(unittest.TestCase):
    driver_path = DRIVER_PATH + '/geckodriver'
    url = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'
    
    locator_searchfield = (By.ID, 'kw')
    locator_searchbutthon = (By.ID, 'su')
    locator_searchresult = (By.XPATH, '//div[contains(@class,"result")]/h3/a')
    
        
    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            self.driver = webdriver.Firefox(executable_path=self.driver_path)
            self.driver.get(self.url)
            self.driver.implicitly_wait(30)
            self.driver.find_element(*self.locator_searchfield).send_keys(d['search'])
            self.driver.find_element(*self.locator_searchbutthon).click()
            result = self.driver.find_element(*self.locator_searchresult)
            logger.info(result.text)
            self.driver.quit()
            

if __name__ == "__main__":
    report = REPORT_PATH + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='Test Report', description='Acceptance test')
        runner.run(Test('test_search'))
    sendmail.mail()
        
        