# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
    #001-导入模块版
'''
import calendar

year = int(input("[1]输入一个年份: "))
if calendar.isleap(year):
    print("{0} 是闰年".format(year)) 
else:
    print("{0} 不是闰年".format(year))

print('=================================')

'''
    #002-常规详细版
'''
year = int(input("[2]输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))
   
print('=================================')

'''
    #003-简化版
'''
year = int(input("[3]请输入一个年份："))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))