#!/usr/bin/python

class MyException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyException('You have a big, big problem')
except MyException:
    print 'Ooops!'
    raise