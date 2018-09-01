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

f = open('..\GameSave\game-01.txt')
score = f.read().split()

Play_rounds = int(score[0])
Total_rounds = int(score[1])
Min_rounds = int(score[2])

print('你已经玩了这个游戏%d次了' % Play_rounds)
print('共计%d个回合' % Total_rounds)
print('最快居然要%d轮才猜出答案' % Min_rounds)
print('真弱呢~人类(笑)')

print('猜猜我现在的数字是多少?')

Player = False
while Player == False:
    answer = int(input())
    Player = bingo(answer, num)
