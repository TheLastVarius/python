#!/usr/bin/python
import math
NOMINALS = [100, 50, 20, 10, 5, 1]

def multipliers(number):
    i = 2
    j = [1]
    while i**2 <= number:
        if number % i == 0:
            while number % i == 0:
                number = number / i
                j.append (i)
            i = i + 1
        else:
            i = i + 1
    j.append (number)
    return j


def equation(a, b, c):
    D = b**2 - 4*a*c
    sqrtD = math.sqrt(D)
    if D >= 0:
        x1 = (-b + sqrtD) / (2 * a)
        x2 = (-b - sqrtD) / (2 * a)
        return x1, x2
    else:
        return 'Нет решения'


def simple(number):
    i = 2
    while i**2 <= number:
        if number % i == 0:
            i = i + 1
        else:
            return "Число простое"
    return "Число составное"

# atm uses only 100, 50, 20, 10, 5 and 1 notes.
def atm(summ):
    result = []
    a = ''
    for n in NOMINALS:
        result.append (summ // n)
        summ = summ % n
    for n in xrange(len(result)):
        if result[n] != 0:    
            a += '%d по %d ' % (result[n], NOMINALS[n])
    return a

print atm(280)

print multipliers(30030)

print equation(2, 19, 35) # 2x^2 + 19x + 35 = 0

print simple(13)

print atm(287)
