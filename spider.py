#!/usr/bin/env python3
# coding: utf-8
# File: spider.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-5-29

from selenium import webdriver
import os
import requests
import time

class SinaIndex:
    '''
    整体趋势：2013-03-01-至今
    移动趋势：2014-01-06-至今
    PC趋势：2014-01-06-至今
    '''
    def __init__(self):
        self.index_page = 'http://data.weibo.com/index'
    '''搜索指数入口'''
    def search_index(self, search_word):
        driver = webdriver.Firefox()
        driver.get(self.index_page)
        e1 = driver.find_element_by_xpath('//input[@node-type="searchInput"]')
        e1.send_keys(search_word)
        e2 = driver.find_element_by_xpath('//a[@node-type="searchBtn"]')
        e2.click()
        return driver

    '''获取指定日期的搜索数据'''
    def get_data(self, driver, start_date, end_date):
        current_url = driver.current_url
        wid = current_url.split('wid=')[-1].split('&wname')[0]
        cookies = driver.get_cookies()
        new_cookies = ''
        for cookie in cookies:
            name = (cookie['name'])
            value = (cookie['value'])
            new_cookie = name + '=' + value + ';'
            new_cookies = new_cookies + new_cookie
        new_cookies = new_cookies[:-1]
        t = time.time()
        time_code = int(round(t * 1000))
        header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie':new_cookies,
            'Host': 'data.weibo.com',
            'Referer':current_url,
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
        }
        url = 'http://data.weibo.com/index/ajax/getchartdata?wid={0}&sdate={1}&edate={2}&__rnd={3}'.format(wid, start_date, end_date, time_code)
        return requests.get(url, headers=header).json()

    '''数据解析'''
    def data_parser(self, data):
        zt_datas = [[item['day_key'], item['value']] for item in data['zt'] if 'day_key' in item]
        pc_datas = [[item['daykey'], item['pc']] for item in data['yd'] if 'daykey' in item]
        mobile_datas = [[item['daykey'], item['mobile']] for item in data['yd'] if 'daykey' in item]
        return zt_datas, pc_datas, mobile_datas

    '''将数据写入到本地文件当中'''
    def write_local_files(self, datas, filepath):
        with open(filepath, 'w+') as f:
            for data in datas:
                f.write(data[0] + ',' + str(data[1]) + "\n")
        f.close()

    '''导出数据'''
    def output_data(self, word, data):
        if not os.path.exists(word):
            os.makedirs(word)
        zt_datas, pc_datas, mobile_datas = self.data_parser(data)
        zt_filepath = '{0}/{1}.txt'.format(word, 'general')
        pc_filepath = '{0}/{1}.txt'.format(word, 'pc')
        mobile_filepath = '{0}/{1}.txt'.format(word, 'mobile')
        self.write_local_files(zt_datas, zt_filepath)
        self.write_local_files(pc_datas, pc_filepath)
        self.write_local_files(mobile_datas, mobile_filepath)

    '''主函数'''
    def index_main(self, word, start_date, end_date):
        print('step1, open page....')
        driver = self.search_index(word)
        print('step2, get data....')
        data = self.get_data(driver, start_date, end_date)
        print(data)
        if data['zt']:
            print('step3, save data ...')
            self.output_data(word, data)
            print('finished....')
        else:
            print('not be record...')
     #   driver.close()

def demo():
    start_date = '2016-05-29'
    end_date = '2018-05-29'
    sina = SinaIndex()
    search_word = '中兴'
    sina.index_main(search_word, start_date, end_date)
demo()