# coding:utf-8
'''
Created on 2018年4月2日

@author: zhanghui
'''
import unittest
import requests


class Test(unittest.TestCase):
    
    
#为了setup和tearDown只执行一次，写为类方法，参数由self变为cls
    @classmethod
    def setUpClass(cls):
        
        print 'Start---'
        
        cls.geturl = 'http://localhost:8081/user/getUser'
        cls.posturl = 'http://localhost:8081/user/postUser'
        cls.data = {
            'userName':'huiwenyuan',
            'phone':'12345'
            }
        cls.jsonurl = 'http://localhost:8081/student/postStu'
        cls.student = {
            'stuName':'张同学',
            'stuClass':'三年二班'
            }
        

    @classmethod
    def tearDownClass(cls):
        print 'End---'


    def testGet(self):
        getReq = requests.get(self.geturl,self.data)
        self.assertEqual(getReq.status_code, 200)
        print getReq.text
        
        
    def testPost(self):
        postReq = requests.post(self.posturl,self.data)
        self.assertEqual(postReq.status_code, 200)
        print postReq.text
        
        
    def testJsonPost(self): 
        postJsonReq = requests.post(self.jsonurl,json=self.student)
        self.assertEqual(postJsonReq.status_code, 200)      
        print postJsonReq.text         


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()