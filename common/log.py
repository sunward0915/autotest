# -*- coding:utf-8 -*-
import logging
import os
from config.data_conf import logpath

LOGLEVEL = logging.DEBUG
# 创建一个logger  
logger = logging.getLogger("mmmm")
logger.setLevel(LOGLEVEL)

# 创建一个handler，用于写入日志文件
global logpath


if not os.path.isdir(logpath):
    os.makedirs(logpath)
logfile = os.path.join(logpath, 'log.txt')
fh = logging.FileHandler(logfile)
fh.setLevel(LOGLEVEL)

# 再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()
ch.setLevel(LOGLEVEL)

# 定义handler的输出格式  
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler  
logger.addHandler(fh)
logger.addHandler(ch)

# 记录一条日志
# url_login = 'https://ptopapi.duozhuan.cn/loginNew/password'
# logger.debug(url_login)
# logger.info('info foorbar')
# logger.warning('warning foorbar')
# logger.error('error  foorbar')
# logger.critical('critical foorbar')
