# coding:utf-8
'''
Created on 2018年4月3日

@author: zhanghui
'''
import unittest
import requests

class Test(unittest.TestCase):
     
    
    def setUp(self):
        print 'Start---'
        self.url = 'http://localhost:8081/user/getUser'
        self.data = {'userName':'huiwenyuan',
                     'phone':'12345'}
      

    def tearDown(self):
        print 'End---'


    def testGet(self):
        req = requests.get(self.url,self.data)
        self.assertEqual(req.status_code, 200, 'request succeed!')
        print req.text


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()