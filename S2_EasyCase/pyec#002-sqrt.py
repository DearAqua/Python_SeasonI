#   user input
num = float(input('input any number'))

#   deal
num_sqrt = num ** 0.5

#   EasyCase#002 square-root-calculate
print('sqrt %0.3f result to %0.3f'%(num ,num_sqrt))


import cmath
 
num = int(input("try complex number"))

num_sqrt = cmath.sqrt(num)

print('{0} square root {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

print(2 ** 4)
