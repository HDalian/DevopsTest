# coding:utf-8
'''
Created on 2018年3月20日

@author: zhanghui
'''

'''
setUp()与tearDown()被称为测试固件，它的主要目标初始化测试用例，执行测试用例后对测试用例执行的结果做后期的处理。
在一个测试类中，如果有N个测试用例，在执行该测试类中的测试用例的时候，会执行N次setUp()和tearDown()
'''
import unittest
from Div import div

class TestDiv(unittest.TestCase):

    def setUp(self):
        print 'Start---'


    def tearDown(self):
        print 'End---'


    def test_001(self):
        self.assertEqual(div(1,1), 1)
        
    def test_002(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)