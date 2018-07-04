#coding:utf-8

'''
Created on 2018年3月19日

@author: zhanghui
'''

# 结合requests 库，看返回的json数据

import json
import requests

r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=西安')

'''
print r.text, u'数据类型：', type(r.text)

dic = json.loads(r.text)

print dic, u'数据类型：', type(dic)
'''

print r.json(), u'数据类型为：', type(r.json())
