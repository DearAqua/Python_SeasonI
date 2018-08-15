#021

# -01-  Fibonacci series: 斐波纳契数列
# -01-01    转行
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
# -01-02    不转行
a, b = 0, 1
while b < 1000:
    print(b, end=' ')
    a, b = b, a+b

print('***************')

# -02-  DogAge series: 狗龄逻辑
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human) 
input("Any key for quit")

print('***************')

# -03-  Bingo Guess: 猜数游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
 
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

print('***************')

# -04-  if in if: if嵌套
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")

