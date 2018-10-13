#   input
a = float(input('The first side:'))
b = float(input('The second side:'))
c = float(input('The third side:'))
 
#   deal
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
 
#   print
print('Area equal %0.2f' %area)
