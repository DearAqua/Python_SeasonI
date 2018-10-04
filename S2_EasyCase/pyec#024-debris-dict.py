# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:49:41 2018

@author: LIZY52
"""

#    debris-020-简化比较操作符
print('')
print('#    debris-020')
testDict = {i: i * i for i in range(10)}
testSet = {i * 2 for i in range(10)}
 
print(testSet)
print(testDict)
   
#    debris-031-简单创建集合
print('')
print('#    debris-031')   
    
#   point
testSet = {i * 2 for i in range(10)}

print(testSet)
      
#    debris-040-简单创建字典
print('')
print('#    debris-040')
      
#   point
testDict = {i: i * i for i in range(10)}

print(testDict)

#    debris-041-列表构建字典
print('')
print('#    debris-041')
t1 = ('吕布','关羽','张飞')
t2 = (100, 99, 99)

#   point 
print(dict (zip(t1,t2)))

#    debris-042-字典构建switch-case
print('')
print('#    debris-042')
      
#   point
def Generalsw(x):
    return Generalsw._system_dict.get(x, None)
 
Generalsw._system_dict = {'吕布': 100, '关羽': 99, '张飞': 99}
 
name = input()
print(Generalsw(name))