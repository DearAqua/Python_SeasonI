def bingo(num1, num2):
    if num1<num2:
        print('太小咯~')
        return False;
    if num1>num2:
        print( '没这么大哦~')
        return False;
    if num1==num2:
        print('bingo！！')
        return True

from random import randint
num = randint(1, 100)

print('猜猜我现在的数字是多少?')

Player = False
while Player == False:
    answer = int(input())
    Player = bingo(answer, num)
