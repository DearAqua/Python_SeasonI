#女票养成日记-#002
level = 10
print('你觉得我颜值有几分?')
User_answer = int(input())
print('===================')
print('branch-01-赞美')
result = User_answer>level
print('别闹，10分制的')
print(result)
print('===================')
print('branch-02-怀疑')
result = User_answer==level
print(User_answer,'分？你偷看我源代码了？')
print(result)
print('===================')
print('branch-03-眼瞎')
result = User_answer<level
print(User_answer,'分!!!眼瞎吗？我马上帮你搜索医院[○･｀Д´･ ○]')
print(result)
