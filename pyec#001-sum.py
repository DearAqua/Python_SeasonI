# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:19:58 2018

@author: lizy52
"""

#   user input
num1 = input('input first number:')
num2 = input('input second number:')

#   sum up
sum1 = float(num1) + float(num2)
cal1 = float(num1) - float(num2)
cal2 = float(num1) * float(num2)
cal3 = float(num1) / float(num2)
cal4 = float(num1) % float(num2)
cal5 = float(num1) // float(num2)

#   EasyCase#001 4-kinds-calculate
print('num {0} add num {1} equal {2}'.format(num1, num2, sum1))

print(cal1,cal2,cal3,cal4,cal5)

#   mix
print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))