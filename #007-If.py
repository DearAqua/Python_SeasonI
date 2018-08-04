level = 10
print('你觉得我颜值有几分?')
User_answer = int(input())
print('===================')
if User_answer>level:
    #print('branch-01-赞美')
    print('别闹，10分制的')

if User_answer==level:
    #print('branch-02-怀疑')
    print(User_answer,'分？你偷看我源代码了？')

if User_answer<level:
    #print('branch-03-眼瞎')
    print(User_answer,'分!!!眼瞎吗？我马上帮你搜索医院')
