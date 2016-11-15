# -*- coding: utf-8 -*-

def my_abs(x):
    if x >=0:
        return x
    elif x<0:
        return -x


n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print my_abs('f')