#!/usr/bin/python

def summ(element1, element2):
    try:
        result = element1 + element2
    except TypeError:
        print 'Неправильный тип элемента'
    else:
        print result
    finally:
        return 'The end'

print summ(1, '2')