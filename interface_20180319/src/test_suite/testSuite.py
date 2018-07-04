# coding:utf-8

'''
Created on 2018年3月20日

@author: zhanghui
'''

import unittest
from test_unittest.TestDiv2 import TestDiv2
from test_report import HTMLTestRunner

suite = unittest.TestLoader().loadTestsFromTestCase(TestDiv2)
runner = HTMLTestRunner.HTMLTestRunner(stream=file('testReport.html','wb'),
                                       title='TestReport',
                                       description=u'测试报告详细信息',
                                       verbosity=2)


runner.run(suite)
#unittest.TextTestRunner(verbosity=2).run(suite)