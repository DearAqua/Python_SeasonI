# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 11:32:45 2018

@author: LIZY52
"""


def cut(num):
    h = 0
    l = 0
    numed = num * 60
    if numed < 65536:
        l = numed
    else:
        h = numed // 65536
        l = numed % 65536
    return h,l

limit = int(input())
num = 500
i = 0

while num <= limit:
    numed = num * 60
    print(i,numed)
    if num < 3000:
        print(cut(num))
        num = num + 250
    elif 3000 <= num < 5000:
        print(cut(num))
        num = num + 500
    else:
        print(cut(num))
        num = num + 1000
    i = i + 1
'''
#    建立初始边界条件
limit = int(input())
num = 500

#    使用 while 循环生成函数
while num <= limit:
    if num < 3000:
        print(num)
        num = num + 250
    elif 3000 <= num < 5000:
        print(num)
        num = num + 500
    else:
        print(num)
        num = num + 1000
'''