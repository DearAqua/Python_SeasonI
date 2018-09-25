# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 11:10:20 2018

@author: LIZY52
"""

def rever(sentence):
    newwords = []
    words = sentence.split()
    words.reverse()
    space = ' '#单词之间一个间隔
    for word in words:
        newword = []
        new = ''#单词的字母间无间隔
        l = len(word)
        for i in range(l):
            newword.append(word[l-i-1])
        neww = new.join(newword)
        newwords.append(neww)
    print(space.join(newwords))
    
rever("what's your problem man ?")