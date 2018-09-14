# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:54:17 2018

@author: lizy52
"""



def TT_c2f(par):
    #    celsius 2 fahrenheit
    result = (par * 1.8) + 32
    return(result)

def TT_f2c(par):
    #    fahrenheit 2 celsius
    result = (par - 32) / 1.8
    return(result)

#   choice
print('choice input type: F:fahrenhet  C:celsius')
select = input()
if select == 'C':
    users = float(input('input celsius: '))
    results = TT_c2f(users)
    print('celsius %0.1f turn to fahrenheit %0.1f ' %(users,results))
elif select == 'F':
    users = float(input('input fahrenheit: '))
    results = TT_f2c(users)
    print('fahrenheit %0.1f turn to celsius %0.1f ' %(users,results))  
else:
    print("Have this type")


'''
#    celsius 2 fahrenheit
celsius = float(input('input celsius: '))
fahrenheit = (celsius * 1.8) + 32
print('celsius %0.1f turn to fahrenheit %0.1f ' %(celsius,fahrenheit))

#    fahrenheit 2 celsius
celsius = float(input('input fahrenheit: '))
celsius = (fahrenheit - 32) / 1.8
print('fahrenheit %0.1f turn to celsius %0.1f ' %(fahrenheit,celsius))
'''