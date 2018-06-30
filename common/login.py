#! /usr/bin/env python
# .py
# -*- encoding:utf-8 -*-
# author: zhangjinming
# date: 2018/5/12 下午5:43

import requests
import hashlib
from common.log import *
from config import data_conf as config

from utils.api_util import set_cookie
import json
import urllib3
urllib3.disable_warnings()

def login_app1():
    #s = requests.session()
    url_login = config.base+ '/loginNew/password'
    #url_login = 'https://ptopapi.duozhuan.cn/loginNew/password'
    #passwd =  generateMD5(pwd)
    '''
    根据接口返回内容,返回特定形式结果json/text
    '''
    params = {'username': config.APP_USER_NAME, 'login_from':'app_i_login', 'password': config.APP_USER_PWD}
    #params = {'username': username, 'login_from': 'app_i_login', 'password': 'qa123321'}
    res = requests.post(url_login, params,verify=False)
    logger.debug('status_code=', res.status_code)
    logger.debug('用户登录结果result=', res)
    if res.status_code == 200:
        ret = res.json()
        logger.debug(ret)
        login_serrsion = ret['data']['session']
        logger.debug('login_serrsion=', login_serrsion)

    else:
        ret = res.json()
        logger.debug('ret=', ret)

def login_app():
    #url_login = 'https://ptopapi.duozhuan.cn/loginNew/password'
    url_login = config.back_url + '/loginNew/password'
    '''
    根据接口返回内容,返回特定形式结果json/text
    '''
    params = {'username': config.APP_USER_NAME, 'login_from':'app_i_login', 'password': config.APP_USER_PWD}
    #params = {'username': username, 'login_from': 'app_i_login', 'password': 'qa123321'}
    logger.debug(url_login)
    logger.debug(params)
    res = requests.post(url_login, params,verify=False)
    # logger.debug('status_code=', res.status_code)
    if res.status_code == 200:
        c = requests.cookies.RequestsCookieJar()
        cookie_dict = res.cookies.get_dict()
        logger.debug(cookie_dict)
        set_cookie(cookie_dict)
        #return cookie_dict
    else:
        #ret = res.json()
        #print('ret=', ret)
        print('fail')
        logger.debug ('fail')

if __name__=="__main__":
    login_app()

