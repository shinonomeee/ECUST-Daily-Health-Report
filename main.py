#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyautogui as pg
from selenium import webdriver
import sys
chrome_opt = webdriver.ChromeOptions()

class Jkrb(object):
    login_url = "http://workflow.ecust.edu.cn/default/work/uust/zxxsmryb/mrybcn.jsp"
    fillin_url = "http://workflow.ecust.edu.cn/default/work/uust/zxxsmryb/mrybtb.jsp"
    accout = "123123"   # input your student number
    pwd = "123123"      # input your password

    def __init__(self):
        print('start\n')
        self.driver = webdriver.Chrome(options=chrome_opt)

    def __del__(self):
        print('completed\n')
        self.driver.close()

    def login(self):
        try:
            self.driver.get(self.login_url)
        except TimeoutError:
            self.driver.close()
            print('超时')
            exit(2)
        self.driver.find_element_by_id('username').send_keys(self.accout)
        self.driver.find_element_by_id('password').send_keys(self.pwd)
        pg.press('enter')
        try:
            self.driver.find_element_by_xpath('//*[@id="fwdjValue"]/div/div/div/div/div/ins').click()
        except:
            self.driver.refresh()
            self.driver.find_element_by_xpath('//*[@id="fwdjValue"]/div/div/div/div/div/ins').click()
        self.driver.find_element_by_id("post").click()


    def start(self):
        self.login()
        try:
            self.driver.find_element_by_xpath('//*[@id="radio_swjkzk13"]/div/ins').click()
        except:
            self.driver.find_element_by_xpath('//*[@id="layui-layer100001"]/div[3]/a').click()
            print('今日已填报')
            exit(1)
        self.driver.find_element_by_xpath('//*[@id="radio_twsfzc5"]/div/ins').click()
        self.driver.find_element_by_xpath('//*[@id="radio_jkmsflm9"]/div/ins').click()
        self.driver.find_element_by_xpath('//*[@id="radio_sfycxxwc27"]/div/ins').click()
        self.driver.find_element_by_id('post').click()
        self.driver.find_element_by_xpath('//*[@id="layui-layer100001"]/div[3]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="layui-layer100002"]/div[3]/a').click()


if __name__ == '__main__':
    jkrb = Jkrb()
    jkrb.start()
    sys.exit()
