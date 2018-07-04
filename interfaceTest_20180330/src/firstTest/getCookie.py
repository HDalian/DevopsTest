# coding:utf-8
'''
Created on 2018年4月3日

@author: zhanghui
'''

import requests

def getCookie():
    
    url='http://localhost:8081/student/getStu'
    data = {
        'stuName':'张同学',
        'stuClass':'三年二班'
        }
    
    req = requests.get(url,data)
    print req.status_code
    print req.headers
    print req.headers['Set-Cookie']
    print req.cookies
    print req.text
    
    
    
if __name__ == '__main__':
    
    getCookie()
        
