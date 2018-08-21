j=0
for i in range(1, 101):
   j = i + j
print(j)

print('输入首项')
x1 = int(input())
print('输入末项')
x2 = int(input())

print((x1+x2)*(x2-x1+1)/2)

ih=0
il=0
for i in range(0, 100):
    ih = i // 10
    il = i % 10
    if ih == 4:
        print('skr')
    elif il == 4:
        print('skr')
    else:
        print(i)
