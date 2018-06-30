#! /usr/bin/env python
# .py
# -*- encoding:utf-8 -*-
# author: gaohuayun
# date: 2018/6/13 下午3:42
# url = "https://ptopapi.duozhuan.cn/forum"
import time
import  unittest
import requests
import json
from common.login import *
from common.log import *
from utils.api_util import *
from config import data_conf as config



class TestFaTie(unittest.TestCase):
    def test_TestFaTie(self):
        u"""发帖"""
        url = config.back_url + '/forum'
        #url = "https://ptopapi.duozhuan.cn/forum"
        #cur_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(time.time()))
        cur_time = get_cur_time('%Y-%m-%d  %H:%M:%S')
        #cookie_login = login.login_app()
        cookie_login = get_cookie()
        logger.debug('获取cookie')
        logger.debug(cookie_login)
        # print('cookie_login =', cookie_login)
        params = {"category": 'p2p',
                  'cid': '0',
                  'sub_category': 'experience',
                  }
        params['title'] = "auto_test自动化测试帖子"
        #params['content']= str(cur_time)+'这是自动化发的帖子有固定的内容，固定的数据'
        params['content']=str(cur_time) + '带图片的帖子帖子展示自己一个人在家好无聊\
        < img\
        src = "/Public/upfile/201806/5b209359d6dbe.png"\
        width = "240"\
        height = "321" / >'
        logger.debug (params['content'])

        # res = requests.post(url, params, cookies =cookie_login,  verify=False)
        res = requests.post(url, params, cookies=cookie_login, verify=False)
        # print('3333，header=' + res.headers)
        # print('status_code='+ res.status_code)
        logger.debug(res.headers)
        logger.debug(res.status_code)
        ret = res.json()
        self.assertEquals(ret['errcode'],config.EXPECT_CODE)
        TieZi_id = ret['data']['insert_id']
        # logger.debug('insert_id='+ TieZi_id)
        print('insert_id=' + TieZi_id)
        set_TieziID(TieZi_id)


    def test_TestTieZiShow(self):
        u"""帖子展示"""
        TieZi_id = get_TieziID()
        url = config.back_url + '/forum/f_'+ str(TieZi_id)
        # url = "https://ptopapi.duozhuan.cn/forum"
        cur_time = get_cur_time('%Y-%m-%d  %H:%M:%S')
        cookie_login = get_cookie()
        logger.debug('test_TestTieZiShow获取cookie')
        logger.debug(cookie_login)
        logger.debug(url)
        # res = requests.post(url, params, cookies =cookie_login,  verify=False)
        res = requests.get(url, cookies=cookie_login, verify=False)
        # print('3333，header=', res.headers)
        # print('status_code=', res.status_code)
        logger.debug(res.headers)
        logger.debug(res.status_code)
        ret = res.json()
        self.assertEquals(ret['errcode'], config.EXPECT_CODE)