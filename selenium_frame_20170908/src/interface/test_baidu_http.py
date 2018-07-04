# coding: utf-8
'''
Created on 2017年9月13日

@author: zhanghui
'''

import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner


class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        self.assertIn('百度一下，你就知道', res.text)


if __name__ == '__main__':
    report = REPORT_PATH + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='Test Report', description='Interface test')
        runner.run(TestBaiDuHTTP('test_baidu_http'))