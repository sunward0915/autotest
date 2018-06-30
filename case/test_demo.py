#! /usr/bin/env python
# .py
# -*- encoding:utf-8 -*-
# author: gaohuayun
# date: 2018/5/19 下午9:58
import  unittest
from common.log import *
import json
class TestDemo(unittest.TestCase):
    # def __init__(self):
    #     logger.debug("TestDemo 开始")
    #     cookie=1

    @classmethod
    def setUpClass(cls):
        logger.debug("setUp 开始")

    @classmethod
    def tearDownClass(cls):
        logger.debug("tearDown 开始")

    def test_TestDemoFunc1(self):
        cookie_login = {'SID': "dadsadas"}
        logger.debug(cookie_login)
        logger.debug(('获取cookie=' + json.dumps(cookie_login)))
        logger.debug ("test_TestDemoFunc11111111")

    def test_TestDemoFunc2(self):
        logger.debug ("test_TestDemoFunc22222222")

