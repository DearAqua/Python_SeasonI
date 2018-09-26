# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:15:20 2018

@author: LIZY52
"""

def Severalord(sentence):
    #   对 sentence 字符串变量进行切片
    words = sentence.split()
    
    #   逐个 word 从 words 中提取
    for word in words:
        #   设定长度
        l = len(word)
        
        #   做单词长度次数个提取
        for i in range(l):
            asciibak = ord(word[l-i-1])
            print(asciibak)

        print('========')

#   实验16位大小写字母兼数字组合
Severalord("EFXA FGWE H124 Dfq7")

print('自定义输入连续字符串')
uesri = input()
uesro = Severalord(uesri)
print(uesro)
