# coding:utf-8
'''
Created on 2018年3月19日

@author: zhanghui
'''

import httplib

def getBaidu():
    http_client = httplib.HTTPConnection('www.baidu.com',80,timeout=20)
    http_client.request('GET', '')
    r = http_client.getresponse()
    
    #print dir(r)
    print r.status
    print r.reason
    print r.getheaders()
    print r.msg
    print r.read()
        
getBaidu()