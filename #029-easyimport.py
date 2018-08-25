#029
#导入模块
import random

#检视模块内函数
dir(random)

#调用其中的函数
random.randint(1, 10)
random.choice([5, 2, 0])

#猜拳哦
var = 1
Ai = 0
print('开始咯~')
while var != 0:
    #   Ai先随机出手，隐藏
    Ai = random.choice([5, 2, 0])
    #   玩家出手后，公布Ai出手
    print('剪刀、石头、布……')
    PlayerTem = input()    
    if Ai == 5:
        print('布~~')
    elif Ai == 2:
        print('剪刀!!')
    elif Ai == 0:
        print('石头~')
    #    判断玩家输入
    if (PlayerTem == '剪刀')|(PlayerTem == '石头')|(PlayerTem == '布'):
        if Ai == 5:
            if PlayerTem == '石头':
                print('切~')
            elif PlayerTem == '剪刀':
                print('我赢啦！！~')
        elif Ai == 2:
            if PlayerTem == '石头':
                print('切~')
            elif PlayerTem == '布':
                print('我赢啦！！~')
        else :
            if PlayerTem == '布':
                print('切~')
            elif PlayerTem == '剪刀':
                print('我赢啦！！~')
    elif PlayerTem == '等下再玩':
        var = 0
    else:
        print('你不会玩嘛？')        
    
    print('再来哦!')
    print('-=-=-=-=-=-=--=-=-=-')
