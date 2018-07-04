# coding:utf-8
'''
Created on 2018年3月19日

@author: zhanghui
'''

import urllib
import urllib2

def get_baidu():
    r = urllib2.urlopen('http://www.baidu.com')
    print r.getcode()
    print r.msg
    print r.headers
    
get_baidu()

def post_cun():
    params = urllib.urlencode({'cityId':'438'})
    r = urllib2.urlopen('http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',params)
    print r.getcode(), r.msg
    print r.read()
    
post_cun()