#! /usr/bin/env python
# .py
# -*- coding:utf-8 -*-
# author: gaohuayun
# date: 2018/6/13 下午3:42
#消息、积分、收藏

import time
import  unittest
import requests
import json
from common.login import *
from common.log import *
from utils.api_util import *
from config import data_conf as config


class TestUserCenter(unittest.TestCase):
    def test_TestMessage(self):
        #消息
        print('PASS')