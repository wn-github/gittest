#/usr/bin/python
#-*-coding:utf-8-*-

#python  时间模块  time  datetime  操作的时间、日期


import time
import datetime

#sleep('浮点数/整数')  休眠
# print('睡眠之前')
# time.sleep(10)
# print('睡眠之后')

#clock()  计算执行代码时CPU花费的的时间
# print(time.clock())

#ctime（） 获取当前时间  asctime（）
# print(time.ctime())
# print(time.asctime())

#输出时间  localtime（）  本地时区
# print(time.localtime())

#格式化输出时间  strftime（'关于时间的字符串'）
# print(time.strftime('%A %B %H: %M: %S'))

# %a  本地化的缩写星期中每日的名称。
#
# %A  本地化的星期中每日的完整名称。
#
# %b  本地化的月缩写名称。
#
# %B  本地化的月完整名称。
#
# %c  本地化的适当日期和时间表示。
#
# %d  十进制数 [01,31] 表示的月中日。
#
# %H  十进制数 [00,23] 表示的小时（24小时制）。
#
# %I  十进制数 [01,12] 表示的小时（12小时制）。
#
# %j  十进制数 [001,366] 表示的年中日。
#
# %m  十进制数 [01,12] 表示的月。
#
# %M  十进制数 [00,59] 表示的分钟。
#
# %p  本地化的 AM 或 PM 。
#
# %S  十进制数 [00,61] 表示的秒。
#
# %U  十进制数 [00,53] 表示的一年中的周数（星期日作为一周的第一天）作为。在第一个星期日之前的新年中的所有日子都被认为是在第0周。
#
# %w  十进制数 [0(星期日),6] 表示的周中日。
#
# %W  十进制数 [00,53] 表示的一年中的周数（星期一作为一周的第一天）作为。在第一个星期一之前的新年中的所有日子被认为是在第0周。
#
# %x  本地化的适当日期表示。
#
# %X  本地化的适当时间表示。
#
# %y  十进制数 [00,99] 表示的没有世纪的年份。
#
# %Y  十进制数表示的带世纪的年份。
#
# %z  时区偏移以格式 +HHMM 或 -HHMM 形式的 UTC/GMT 的正或负时差指示，其中H表示十进制小时数字，M表示小数分钟数字 [-23:59, +23:59] 。
#
# %Z  时区名称（如果不存在时区，则不包含字符）。
#
# %%  字面的 '%' 字符。



#strptime('关于时间的字符串')  格式化解析字符串
"""
%y  年份
%d  一个月中第几天
%b  表示的是月份
"""
# print(time.strptime('30 Nov 00','%d %b %y'))

#计算机元年到现在所有秒的总和 time（）
# print(time.time())










#datetime
from datetime import datetime, date, timedelta   #精确导入
# import datetime  #整体导入

#获取当前时间、日期   datetime.now()
# print(datetime.now())

#获取指定的时间、日期   datetime(数字【整数】)
# print(datetime(2019, 7, 30, 12, 1, 1))

#将时间字符串：2019-07-30 12:01:01
# 转成datetime里的日期：2019-07-30 12:01:01
#  strptime（）
a = datetime.strptime('1937-7-7 12:00:00','%Y-%m-%d %H:%M:%S')
print(a)

#将日期转换为字符串 strftime（）
b = datetime.now().strftime('%H:%M:%S')
print(b)

#日期的加减
#求当前时间
c = datetime.now()
print(c)
#小时 hours = 3 天  days = 3   分  minutes = 3  秒  seconds = 3
d = c + timedelta(minutes=3)
print(d)

#获取当前日期   today（）   ---->  2019-07-30
print(date.today())

#对日期进行加减
#步骤一：获取当前的日期
#步骤二：加减日期  timedelta（days = xxx）
e = date.today() + timedelta(days=1)
print(e)


























