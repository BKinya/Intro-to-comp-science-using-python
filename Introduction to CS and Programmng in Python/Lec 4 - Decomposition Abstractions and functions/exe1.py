# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 07:41:33 2019

@author: user
"""

#def func_a():
#    print('inside func a')
#
#def func_b(z):
#    print('inside func b')
#    return z()

#print(func_b(func_a))

## closure and factory method
def generate_power(number):
    def nth_power(power):
        return number ** power
    return nth_power

z = generate_power(2)
print(z(8))
        