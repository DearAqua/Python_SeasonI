# Initialize
from random import randint
emotion = randint (1, 100)
branch_s1 = False
branch_s2 = False
branch_s3 = False
level = 10
time = 0
#Interaction
print('你今天心情好吗？')

if emotion >= 75:
    #branch-s1心情很好的分支
    print('今天遇到好事了呢~我和你说啊...')
    while branch_s1 == False:            
        User_answer = input()
        print('blablabalbla...')
if 75 > emotion >=50:        
    #branch-s2心情较好的分支
    print('嗯嗯~有事嘛？')
    while branch_s2 == False:            
        User_answer = input()
        print('blabla...')
if 50 > emotion >=25:        
    #branch-s3心情一般的分支
    print("不太好，话说你觉得我颜值有几分?")
    while branch_s3 == False:            
        User_answer = int(input())
        if time == 3:
            branch_s3 = True
        if time != 3:
            if User_answer>level:
                #print('branch-s3-01-赞美')
                print('别闹，10分制的')
                time = time + 1
            if User_answer==level:
                #print('branch-s3-02-怀疑')
                print(User_answer,'分？你偷看我源代码了？')
                time = time + 1
            if User_answer<level:
                #print('branch-s3-03-眼瞎')
                print(User_answer,'分!!!眼瞎吗？我马上帮你搜索医院[○･｀Д´･ ○]')
                time = time + 1
    print("你好烦啊~自己的女票都不会哄嘛？")
if emotion < 25:
    #branch-s4心情很差的分支
    print('走开~不想理你')
    


