# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:57:53 2018

@author: LIZY52
"""

#    debris-050-合并多个字符串
print('')
print('#    debris-050')
test = ['给', '你', '很多', '小心心']
space = ' '

#   point
print(' '.join(test))
print(space.join(test))

#    debris-051-倒序函数
print('')
print('#    debris-051')
testList = ['哎', '呀', '呀']

#   point
testList.reverse()

print(testList)

#    debris-052-For循环倒序输出
print('')
print('#    debris-052')
      
#   point
for element in reversed([2,3,3]):
    print(element)

#    debris-053-列表切片倒序
print('')
print('#    debris-053')
      
#   point    
print("你的下一句话是不是：标准结局"[::-1])