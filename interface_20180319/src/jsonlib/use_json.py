#coding:utf-8

'''
Created on 2018年3月19日

@author: zhanghui
'''

import json


dict1 = {'name':'zh', 'age':'32', 'address':'beijing'}

print u'未序列化前的数据类型为：', type(dict1)
print u'未序列化前的数据：' , dict1

#json.dumps 用于将 Python 对象编码成 JSON 字符串
str1 = json.dumps(dict1)

print u'序列化后的数据类型为：', type(str1)
print u'序列化后的数据：' , str1

#json.loads 将已编码的 JSON 字符串解码为 Python 对象
dict2 = json.loads(str1)

print u'反序列化后的数据类型为：', type(dict2)
print u'反序列化后的数据：' , dict2

