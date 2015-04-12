#!/usr/bin/python
import random

def letters(big_string):
    b = ''
    a = big_string.lower()
    for n in xrange(len(a)):
        if a[n] != big_string[n]:
            b += '%s' %(big_string[n])
    return b.strip()


def palindrome(pali):
    a = len(pali)
    if a % 2 == 0:
        a = a / 2
    else:
        a = (a - 1) / 2
    b = pali[:a]
    c = pali[:(-a - 1)]
    if b == c:
        return 'палиндром'
    else:
        return 'не палиндром'


def find_letter(where, letter):
    a = where.split()
    b = []
    for n in a:
        if n[0] == letter:
            b.append (n)
    return ' '.join(b)


def mix_words(just_string):
    a = just_string.split(' ')
    random.shuffle(a)
    return ' '.join(a)


print letters("Trees Are So Kind")

print palindrome("avid diva")

print find_letter("Bears are the best animals ever", 'b')

print mix_words("Bears are the best animals ever")
