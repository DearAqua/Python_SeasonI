#    debris-000-互换赋值
print('#    debris-000')
x,y = 10,20
print(x,y)

#   point
x,y = y,x

print(x,y)

#    debris-001-三元操作符
print('')
print('#    debris-001')
print('输入y值(正整数)')
y = int(input())

#   point
x = 10 if (y == 9) else 20

print(x)

#    debris-002-列表元素赋值到变量
print('')
print('#    debris-002')
testList = [5,6,7]

#   point
x, y, z = testList
 
print(x, y, z)

#    debris-010-简化链状比较操作符
print('')
print('#    debris-010')
print('输入n值(正整数)')
n = int(input())

#   point
result = 1 > n <= 9

print(result)

#    debris-011-简化if语句
print('')
print('#    debris-021')
m = int(input())
if m in [1,3,5,7]:
    print('true')
else:
    print("What's Up? Silly boy?")
