# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 08:59:45 2018

@author: LIZY52
"""
#    Str.is Series
print('Test 1')
str = "the str are all ..."
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r
print("------------------------")

print("Test 2")
str = "iswhat"
print(str.isalnum()) 
print(str.isalpha()) 
print(str.isdigit()) 
print(str.islower()) 
print(str.isupper()) 
print(str.istitle()) 
print(str.isspace()) 

trystring = input()
print(trystring.isalnum())