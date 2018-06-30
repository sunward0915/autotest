#! /usr/bin/env python
# .py
# -*- coding:utf-8 -*-
# author: zhangjinming
# date: 2018/5/12 5:39

#引进基础类库
from case.test_faTie_no_picture import Test_FaTie_No_Picture
from common.login import login_app
from utils.HTMLTestRunner import *
from utils.api_util import *

#前置登录
login_app()
# exit(1)

#添加测试用例
suite = unittest.TestSuite()
# suite.addTest(TestFaTie("test_TestFaTie"))
# suite.addTest(TestFaTie("test_TestTieZiShow"))
# suite.addTest(TestDemo("test_TestDemoFunc1"))
# suite.addTest(TestDemo("test_TestDemoFunc2"))

suite.addTest(Test_FaTie_No_Picture("test_TestFaTie"))
suite.addTest(Test_FaTie_No_Picture("test_TestTieZiShow"))


#定制报告的目录及文件前缀

report_FileName = getReportFileName()
fp = open(report_FileName, 'wb+')
print('生成报告中，耐心等待.....')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试', description='接口测试详情')
runner = HTMLTestRunner(stream=fp, title='接口测试', description='接口测试详情')
runner.run(suite)
fp.close()

print('生成测试报告')
