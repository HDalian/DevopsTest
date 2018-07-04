# coding: utf-8
'''
Created on 2017年9月13日

@author: zhanghui
'''
from selenium.webdriver.common.by import By
from common.page import Page

class BaiDuMainPage(Page):
    
    loc_search_input = (By.ID, 'kw')
    loc_search_button = (By.ID, 'su')
    
        
    def search(self,kw):
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()
    