#!/usr/bin/python
#coding=utf-8


import random
import time
import os


#Собственное исключение

class MyException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#Функция, возвращающая несколько значений

#Возвращает сумму и разницу переданных аргументов

def enum(elem1, elem2):
    return elem1 + elem2, elem1 - elem2


#Генератор

#Имитатор броска монетки, орел или решка.

def heads_tails():
    yield random.randint(0,1)


#Примеры lambda, nested function и closure

#Вложенная lambda функция, суммирующая оба передаваемых аргументы, вызывается внутри функции nested_sum

def nested_sum(element1, element2):
    result = lambda element1, element2: element1 + element2
    return result(element1,element2)
    

#Тоже самое, что и выше, только через замыкание. Замыкание возвращает нам lambda функцию, суммирующую аргументы

def closure_sum(element1):
    result = lambda element2: element1 + element2
    return result


#Примеры *args, **kwargs, optional и named

#Суммирование всех передаваемых аргументов с помощью *args

def args_sum(*args):
    result = 0
    for number, element in enumerate(args):
        result += element
    return result


#Суммирование всех значений передаваемого словаря с помощью **kwargs

def kwargs_sum(**kwargs):
    result = 0
    for key, value in kwargs.items():
        result += value
    return result


#Суммирование передаваемых аргументов, с использованием optional и named

def optional_sum(element1, element2 = 2, element3 = 10):
    return  element1 + element2 + element3


#Декораторы

#Декоратор, показывающий время работы функции

def timer(function):
    def wraper(*args,**kwargs):
        t = time.time()
        result = function(*args, **kwargs)
        text = 'Время работы функции = %f' %(time.time() - t)
        print result
        print text
    return wraper


#Декоратор, показывающий имя функции

def name(function):
    def wraper(*args,**kwargs):
        print 'Имя функции %s' %function.__name__
        print function(*args,**kwargs)
    return wraper


#Декоратор, запрещающий выполнение функции, если скрипт запущен не от указанного пользователя

def user(function):
    def wraper(*args,**kwargs):
        if os.getlogin() == 'niki':
            print function(*args,**kwargs)
        else:
            raise MyException('You shall not pass')
    return wraper


#Декоратор, ничего не делающий, если функция вернула True и вызывающий эксепшен, если функция вернула строка

def exception(function):
    def wraper(*args,**kwargs):
        result = function(*args,**kwargs)
        if result is not True:
            if type(result) == str:
                raise MyException(result)
        else:
            print function(*args,**kwargs)
    return wraper


print 'Функция, возвращающая несколько значений:'
item1, item2 = enum(5, 2)
print item1, item2


print 'Бросок монетки:'
for element in heads_tails():
    if element == 0:
        print 'Орел'
    else:
        print 'Решка'


print 'Вложенная функция + lambda:'
print nested_sum(1, 2)

print 'Замыкание + lambda:'
sum_with = closure_sum(1)
print sum_with(2)


print '*args:'
print args_sum(1,2,3,4,5)

print '**kwargs:'
print kwargs_sum(one = 1, two = 2, three = 3, four = 4, five = 5)

print 'optional & named:'
print optional_sum(3,element3=2)


print 'Декораторы:'

#Убрать коммент с нужной строки, для проверки конкретного декоратора
#Использование вложенных декораторов мне кажется не желательным, потребуются костыли, чтобы все отработало нормально.
#@timer
#@name
#@user
#@exception
def sum(element1, element2):
    return 'Result: %i' %(element1 + element2)

sum(25,31)