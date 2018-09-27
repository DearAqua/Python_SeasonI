# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 10:33:39 2018

@author: LIZY52
"""

def cut(num):
    h = 0
    l = 0
    if num < 65536:
        l = num
    else:
        h = num // 65536
        l = num % 65536
    return h,l

#   self-test
#   useri = 65537
#   print(cut(useri))

#   freedom input
circle = 1
while circle == 1:
    useri = int(input()) * 60
    print(cut(useri))


