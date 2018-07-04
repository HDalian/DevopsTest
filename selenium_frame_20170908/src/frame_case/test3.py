# coding: utf-8
'''
Created on 2017年9月8日

@author: zhanghui
'''
'''
test3.py 
封装xlrd模块，读取excel，实现用例的参数化。
在utils层的file_reader中添加ExcelReader读取Excel文件
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.log import logger

from utils.config import Config, DRIVER_PATH, DATA_PATH
from utils.file_reader import ExcelReader


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
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()