# coding:utf-8

'''
Created on 2018年3月19日

@author: zhanghui
'''
#当与文件操作结合时，使用json.dump、json.load

import json

list1 = ['selenium', 'appium', 'android', 'ios']

#把list1先序列化，再写入到一个文件中
print json.dump(list1, open('/Users/zhanghui/Documents/Python outputs/jsonOutput.txt','w'))
print u'文件内容为：'

r = open('/Users/zhanghui/Documents/Python outputs/jsonOutput.txt', 'r+')
print r.read()

#先读取文件内容，再进行反序列化
res = json.load(open('/Users/zhanghui/Documents/Python outputs/jsonOutput.txt', 'r+'))
print res, u'数据类型：', type(res)
