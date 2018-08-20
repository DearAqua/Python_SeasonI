level = 10
time = 0
result= False
print("你觉得我颜值有几分?")
while result == False:
    User_answer = int(input())
    if time == 3:
        result = True
    if time != 3:
        if User_answer>level:
            #print('branch-01-赞美')
            print('别闹，10分制的')
            time = time + 1
        if User_answer==level:
            #print('branch-02-怀疑')
            print(User_answer,'分？你偷看我源代码了？')
            time = time + 1
        if User_answer<level:
            #print('branch-03-眼瞎')
            print(User_answer,'分!!!眼瞎吗？我马上帮你搜索医院[○･｀Д´･ ○]')
            time = time + 1
print("你好烦啊~自己的女票都不会哄嘛？")


