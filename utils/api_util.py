#! /usr/bin/env python
# .py
# -*- coding:utf-8 -*-
# author: zhangjinming
# date: 2018/5/12 下午5:41
"""
接口测试基础方法封装
"""

import hashlib
import time
import os
from config.data_conf import PROJECT_DIR
login_cookie = {}
TieZi_id=""

###### 发送http请求 START ######
def generateMD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()

def get_cur_time(format_style):
    cur_time = time.strftime(format_style, time.localtime(time.time()))
    return cur_time

def get_cookie():
    global login_cookie
    return login_cookie

def set_cookie(cookie):
    global login_cookie
    login_cookie = cookie

def get_TieziID():
    global TieZi_id
    return TieZi_id

def set_TieziID(id):
    global TieZi_id
    TieZi_id = id

#定制报告的目录及文件前缀
def getReportFileName():
    print ('工程路径projectDir=', PROJECT_DIR)
    resultDir_expect = PROJECT_DIR + r'/result'
    if not os.path.exists(resultDir_expect):
        resultDir = os.makedirs(resultDir_expect)
    print ('报告路径=', resultDir_expect)
    report_name = 'report_' + get_cur_time('%Y%m%d%H%M%S') + '.html'
    print('报告文件名', report_name)


    full_file_name = os.path.join(resultDir_expect,report_name)
    return full_file_name