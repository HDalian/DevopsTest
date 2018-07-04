# coding: utf-8
'''
Created on 2017年9月8日

@author: zhanghui
'''

#读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。

from utils.file_reader import YamlReader
import os

BASE_PATH = '/Users/zhanghui/Documents/SeleniumResources/'
#BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yaml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

class Config(object):
    
    def __init__(self,config=CONFIG_FILE):
        self.config = YamlReader(config).data
    
    def get(self,key):
        return self.config.get(key)
    
if __name__ == '__main__':
    c = Config()
    print c.get('URL')


        