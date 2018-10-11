
'''
def cut(num):
    h = 0
    l = 0
    numed = num * 60
    if numed < 65536:
        l = numed
    else:
        h = numed // 65536
        l = numed % 65536
    return h,l

limit = int(input())
num = 500

while num <= limit:
    numed = num * 60
    print(numed)
    if num < 3000:
        print(cut(num))
        num = num + 250
    elif 3000 <= num < 5000:
        print(cut(num))
        num = num + 500
    else:
        print(cut(num))
        num = num + 1000
'''

def AutoQcode(num):
    l = 0
    numed = num * 60
    if numed < 65536:
        l = numed - 10
    else:
        l = numed % 65536 - 10
    return l

def coding(var):
    l = len(str(var))
    for i in range(l):
        bak = var // (10 ** (l-i-1))
        var = var % (10 ** (l-i-1))
        #print(bak)
        print('KeyPress "%d", 1'%(bak))
    print('//======')

limit = int(input())
print('以上是输入')
num = 500
var = 0

while num <= limit:
    numed = num * 60
    print(numed)
    print('//======')
    if num < 3000:
        var = AutoQcode(num)
        coding(var)
        num = num + 250
    elif 3000 <= num < 5000:
        var = AutoQcode(num)
        coding(var)
        num = num + 500
    else:
        var = AutoQcode(num)
        coding(var)
        num = num + 1000
    
