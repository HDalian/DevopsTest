# coding:utf-8
'''
Created on 2018年3月20日

@author: zhanghui
'''
'''
解决让测试固件setUp、tearDown只执行一次，让测试固件使用类方法
'''
import unittest
from Div import div

class TestDiv2(unittest.TestCase):

#setUp后面输入Class，自动匹配类方法格式
    @classmethod
    def setUpClass(cls):
        print 'Start---'


    @classmethod
    def tearDownClass(cls):
        print 'End---'


    def test_001(self):
        self.assertEqual(div(1,1), 1)
        
    def test_002(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)