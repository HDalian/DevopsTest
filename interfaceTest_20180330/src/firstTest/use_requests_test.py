# coding:utf-8
'''
Created on 2018年4月2日

@author: zhanghui
'''

import requests


def requestsGet():
    
    url = 'http://localhost:8081/user/getUser'
    params = {'userName':'huiwenyuan',
              'phone':'12345'}
    
    r1 = requests.get(url,params)
    print r1.status_code
    print r1.text
    print r1.headers
    print r1.headers['Content-Type']


def requestsPost():
    
    url = 'http://localhost:8081/user/postUser'
    data = {'userName':'huiwenyuan',
            'phone':'54321'}
    
    r2 = requests.post(url,data)
    print r2.status_code
    print r2.text
   

def requestsJsonPost():
    
    url = 'http://localhost:8081/student/postStu'
    
    data = {'stuName':'张同学',
            'stuClass':'三年二班'}

    #不需要json.dumps()和headers，requests有json=  
    r3 = requests.post(url,json=data)
    print r3.status_code
    print r3.text

    
if __name__ == '__main__':
    
    requestsGet()
    requestsPost()
    requestsJsonPost()
        