Var_F = (1 == 3)
print(Var_F)
Var_T1,Var_T2 = 200, 300
print(Var_T1 < Var_T2)
print("====================")
print("回车再继续")
input()
RedStone_S1 = not Var_F
RedStone_S2 = Var_F and True
RedStone_S3 = Var_F or False
print(RedStone_S1)
print(RedStone_S2)
print(RedStone_S3)
print("====================")
num = 10
print('Guess what I think?')
answer = int(input())
result = answer
print('too small?')
print(result)
result = answer>num
print('too big?')
print(result)
result = answer==num
print('equal?')
print(result)
