for letter in 'Python':
   if letter == 'h':
      continue
   print('当前字母 :', letter)

var = 10
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('当前变量值 :', var)


ih=0
il=0
for i in range(0, 100):
    ih = i // 10
    il = i % 10
    if ih == 4:
        continue
    elif il == 4:
        continue
    else:
        print(i)



n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
