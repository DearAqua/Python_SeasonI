# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:36:09 2018

@author: LIZY52
"""
    
def txt(sentence):
    words = sentence.split()
    space = ' '
    obak = []
    for word in words:
        bak = []
        l = len(word)

        for i in range(l):
            newword = ord(word[l-i-1])
            bak.append(str(newword))
            #   print(newword)
        bak.reverse()
        print(space.join(bak))
        obak.append(str(bak))
#   txt('ABCD1234')

print('自定义输入连续字符串')
uesri = input()
txt(uesri)