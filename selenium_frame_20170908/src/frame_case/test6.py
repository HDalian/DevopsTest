# coding: utf-8
'''
Created on 2017年9月13日

@author: zhanghui
'''
'''
test6.py
将test封装为case、common、page、suite
test
    |--case（用例文件）
    |--common（跟项目、页面无关的封装）
    |--page（页面）
    |--suite（测试套件，用来组织用例）
'''

import unittest
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils import sendmail

from page.baidu_main_page import BaiDuMainPage
from page.baidu_result_page import BaiDuResultPage


class Test(unittest.TestCase):
    url = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'
    
    
    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            self.test = BaiDuMainPage(browser_type='chrome')
            self.test.get(self.url, maximize_window=False)
            self.test.search(d['search'])
            self.test = BaiDuResultPage(self.test)
            self.test.result()
            logger.info(self.test.result().text)
            self.test.save_screen_shot()
            self.test.quit()


if __name__ == "__main__":
    report = REPORT_PATH + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='Test Report', description='Acceptance test')
        runner.run(Test('test_search'))
    sendmail.mail()