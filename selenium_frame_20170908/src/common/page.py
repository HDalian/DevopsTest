# coding: utf-8
'''
Created on 2017年9月13日

@author: zhanghui
'''

from common.browser import Browser


class Page(Browser):


    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)
            
    def get_driver(self):
        return self.driver
    
    def find_element(self,*args):
        return self.driver.find_element(*args)
    
    def find_elements(self,*args):
        return self.driver.find_elements(*args)

    