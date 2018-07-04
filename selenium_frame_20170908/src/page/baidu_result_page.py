# coding: utf-8
'''
Created on 2017年9月13日

@author: zhanghui
'''

from selenium.webdriver.common.by import By
from common.page import Page


class BaiDuResultPage(Page):
    loc_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def result(self):
        return self.find_element(*self.loc_result)
    