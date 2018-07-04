# coding:utf-8
'''
Created on 2018年4月2日

@author: zhanghui
'''

import urllib
import urllib2
import json

def firstGetTest():
    
    url = 'http://localhost:8081/user/getUser'

    data = {}
    data['userName'] = 'huiwenyuan'
    data['phone'] = '12345'
    data = urllib.urlencode(data)

    getReq = url + '?' + data
    reqResponse = urllib2.urlopen(getReq)
    responseStr = reqResponse.read()
    responseStr = responseStr.decode('unicode_escape')
    
    print (responseStr)
    


def firstPostTest():
    
    url = 'http://localhost:8081/user/postUser'

    data = {}
    data['userName'] = 'huiwenyuan'
    data['phone'] = '54321'
    data = urllib.urlencode(data)

    postReq = urllib2.Request(url,data)
    reqResponse = urllib2.urlopen(postReq)
    responseStr = reqResponse.read()

    print (responseStr)
    

def postJsonTest():
    
    url = 'http://localhost:8081/student/postStu'

    headers = {'Content-Type': 'application/json'}
    data = {
        'stuName': 'huiwenyuan',
        'stuClass': '三年二班'}

    jsondata = json.dumps(data)

    # 注意Request参数顺序
    req = urllib2.Request(url,jsondata,headers)
    reqResponse = urllib2.urlopen(req)
    responseStr = reqResponse.read()

    print (responseStr)
    
if __name__ == '__main__' :
    firstGetTest()
    firstPostTest()
    postJsonTest()