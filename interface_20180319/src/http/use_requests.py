# coding:utf-8
'''
Created on 2018年3月20日

@author: zhanghui
'''


import requests

r1 = requests.get(
    url='http://yuedu.baidu.com/ebook/3c0077aaa32d7375a41780bb',
    params={'_searchquery':'selenium-python%D7%D4%B6%AF%BB%AF%B2%E2%CA%D4'}
    )

print r1.url

r2 = requests.post(
    url='http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',
    data={'cityId':438}
    )

print r2.json()