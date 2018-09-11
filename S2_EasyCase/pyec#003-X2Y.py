'''
#   import
import cmath

#   input
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
 
#   deal
print('{0:0.1f}x**2 + {1:0.1f}x + {2:0.1f} = 0'.format(a,b,c))

d = (b**2) - (4*a*c) 

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

#   print
print('reuslt: {0} and {1}'.format(sol1,sol2))

'''

#   EasyCase#003 Qquadratic Equation
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

d = (b**2) - (4*a*c)

sol1 = (-b-d**0.5)/(2*a)
sol2 = (-b-d**0.5)/(2*a)

print('x1={0},x2={1}'.format(sol1,sol2))
