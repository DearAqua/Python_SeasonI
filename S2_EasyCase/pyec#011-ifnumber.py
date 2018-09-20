# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:10:16 2018

@author: lizy52
"""
#   自定义函数
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
print('测试字符串和数字')
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True

print('============================') 

print('测试 Unicode')
print('阿拉伯语 5')
print(is_number('٥'))  # True
print('泰语 2')
print(is_number('๒'))  # True
print('中文数字')
print(is_number('四')) # True
print('版权号')
print(is_number('©'))  # False

trystring = input()
print(is_number(trystring))
