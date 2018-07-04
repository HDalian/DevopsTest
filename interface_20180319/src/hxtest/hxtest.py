# coding:utf-8
'''
Created on 2018年3月20日

@author: zhanghui
'''
import unittest
import requests
import json


class Test(unittest.TestCase):


    def setUp(self):
        self.url = 'http://lz.huaxiaexpress.com'


    def tearDown(self):
        pass


    def testName(self):
        params={'pname':'hxbjzh',
              'upwd':'569760',
              'sign':'0',
              't':'0.1335552114255421'
              }
        self.r = requests.get(self.url+'/User/login',params)
        
        print self.r.url
        print self.r.text
        
        #return {'user id':self.r.json()['data']['user id']}

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()