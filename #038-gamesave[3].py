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

#   Name
Player_name = input('愚蠢的人类啊~给我报上你的名字：')

#   Load
f = open('..\GameSave\game-01.txt')
lines = f.readlines()
f.close()

scores = {}
for l in lines:
   s = l.split()
   scores[s[0]] = s[1:]
score = scores.get(Player_name)

if score is None:
        score = [0,0,0]
        
Play_times = int(score[0])
Total_rounds = int(score[1])
Min_rounds = int(score[2])

#   Initialize
if Play_times == 0:
    print('第一次玩？懂规则吗人类？开始咯~')
else:
    print('%s 你已经玩了这个游戏%d次了' % (Player_name,Play_times))
    print('共计%d个回合' % Total_rounds)
    print('最快居然要%d轮才猜出答案' % Min_rounds)
    print('真弱呢~人类(笑)')

print('猜猜我现在的数字是多少?')

rounds = 0
Player = False

while Player == False:
    rounds += 1
    answer = int(input())
    Player = bingo(answer, num)

#   Deal
#   01最快记录
if Min_rounds == 0 or rounds < Min_rounds:
   Min_rounds = rounds
#   02发起次数
Play_times += 1
#   03总回合数
Total_rounds += rounds

#   Save
scores[Player_name] = [str(Play_times), str(Total_rounds), str(Min_rounds)]
result = ''
for n in scores:
   line = n + ' ' + ' '.join(scores[n]) + '\n'
   result += line

f = open('..\GameSave\game-01.txt', 'w')
f.write(result)
f.close()
