#/usr/bin/python
#-*-coding:utf-8-*-# python日志模块 logging内置模块
"""
日志的作用？
记录代码在执行的过程中重要步骤地运行时产生的信息
日志等级：由低到高
NOTSET：0
DEBUG：10
INFO：20
WARRING：30
ERROR：40
CRITICAL：50
"""

import logging
# import coloredlogs  # 第三方模块，将日志信息变成彩色的输出


# 自定义
# from untils.Base import LOG_DIR
# 导入时间模块
from datetime import datetime

# 获取当前文件名字__name__
logger = logging.getLogger(__name__)

# 输出日志信息到两个位置
# 时间.后缀名 2019-09-06.txt

# print(datetime.now().date())

# 创建日志文件
log_name = str(datetime.now().date()) + '.out'

# 输出到控制台
s_handler = logging.StreamHandler()

# 输出到文件
f_handler = logging.FileHandler(filename=log_name,encoding='utf-8')



# 设置日志输出到控制台的等级
logger.setLevel(logging.DEBUG)
# s_handler.setLevel(logging.DEBUG)
#
# # 设置日志输出到文件的等级
# f_handler.setLevel(logging.DEBUG)

# 设置日志格式
"""
asctime 当前时间
name 脚本名字
levelname 日志等级
massage 日志记录的信息
"""
f_formatter = logging.Formatter(
"%(asctime)s %(name)s %(levelname)s %(message)s"
)

# 添加日志格式
s_handler.setFormatter(fmt=f_formatter)
f_handler.setFormatter(fmt=f_formatter)

# 添加日志控制器 --->  开关
logger.addHandler(f_handler)
logger.addHandler(s_handler)



# 写日志
logger.info('adgagadgah')
logger.debug('lkjnhkjnhk')
logger.error('kjnhjkgjhvf')
logger.critical('uwoukrins,ma')





























