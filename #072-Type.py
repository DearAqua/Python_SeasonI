#!/usr/bin/python3

#Vivi 单个赋值
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "string"     # 字符串

print (counter)
print (miles)
print (name)

#Vivi 多个赋值

a = b = c = 1
print(a,b,c)

a, b, c = 1, 2, "string"
print(a,b,c)

#Vivi 数字类型
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))

print(isinstance(d, int))

print(5 + 4)   # 加法

print(4.3 - 2) # 减法

print(3 * 7)   # 乘法

print(2 / 4)   # 除法，得到一个浮点数

print(11 // 3)  # 除法，得到一个整数

print(11 % 3)  # 取余

print(2 ** 5)  # 乘方
