'''
def factoria(n):
    if n==1:
        return 1
    return n * factoria(n - 1)
'''

def factoria(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

n = int(input())
print(factoria(n))

j = 1
m = int(input())
for i in range(1, m+1):    
    j = j * i
    print(j)