#!/usr/bin/python
#coding=utf-8


import itertools
result = []


#Три примера list comprehensions, возвращающих итератор
#Модификация списка, использование условия и использование двух списков

#Возводит в квадрат элементы первого списка, возводит в квадрат четные элементы второго списка
#Подает на вывод квадрат тех элементов из первого списка, которые есть во втором списке

def iter(catalog1, catalog2):
    catalog1 = [item ** 2 for item in catalog1]
    catalog2 = [item ** 2 for item in catalog2 if item % 2 == 0]
    return [item ** 2 for item in catalog1 if item in catalog2]


#Три примера list comprehensions, возвращающих генератор

#Модификация списка
#Возводит в квадрат элементы первого списка
#Оставил в качестве входного параметра оба списка, для наглядности сравнения

def gener0(catalog1,catalog2):
    catalog1 = (item ** 2 for item in catalog1)
    return catalog1


#Использование условия
#Возводит в квадрат четные элементы второго списка

def gener1(catalog1,catalog2):
    catalog2 = (item ** 2 for item in catalog2 if item % 2 == 0)
    return catalog2


#Использование двух списков
#Возводит в квадрат те элементы первого списка, которые есть во втором списке

def gener2(catalog1, catalog2):
    return (item ** 2 for item in catalog1 if item in catalog2)


#Пять примеров использования itertools

#Шифр

def secret(text, key):
    return itertools.compress(text, key)


#Слияние разных по длине списков в один кортеж

def zipper(catalog1, catalog2):
    return itertools.izip_longest(catalog1, catalog2)


#Повторение элемента

def repeat(element, count):
    return itertools.tee(element, count)


#Применение функции ко всем элементам

def appl(function, element1, element2):
    return itertools.imap(function, element1, element2)


#Слияние двух списков в один

def merger(catalog1, catalog2):
    return itertools.chain(catalog1,catalog2)


print 'list comprehensions, возвращающие итератор:'

print iter([1,2,3],[2,3,4,9])


print 'list comprehensions, возвращающие генератор:'

print 'модификация списка:'
for item in gener0([1,2,3],[2,3,4,6]):
    print item

print 'использование условия:'
for item in gener1([1,2,3],[2,3,4,6]):
    print item

print 'использование двух списков:'
for item in gener2([1,2,3],[2,3,4,6]):
    print item


print 'пять примеров использования itertools:'

print 'compress:'
print ''.join([item for item in secret('asHwqcSCecSclcseflCSo,ca cmaHNscdOasyda ddaseaAdDSVdard dfdasrfisaedASdnddassd', [0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0])])

print 'izip_longest:'
for item in zipper([1,2,3,4], ['a','b','c']):
    print item

print 'tee:'
for item in repeat(['Hello'], 5):
    result.append([item for item in item])
print result

print 'imap:'
for item in appl(pow, [2,3], [5,4]):
    print item

print 'chain:'
print ''.join(item for item in merger(['a','b','c'], ['d','e','f']))