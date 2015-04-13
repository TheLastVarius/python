#!/usr/bin/python
import random

def letters(big_string):
    res = ''
    low = big_string.lower()
    zipped = zip(big_string,low)
    for z in zipped:
        if z[0] != z[1]:
            res += '{}'.format(z[0])
    return res.strip()


def palindrome(pali):
    if pali == pali[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


def find_letter(where, letter):
    splitter = where.split()
    res = []
    for s in splitter:
        if s[0].lower() == letter:
            res.append (s)
    return ' '.join(res)


def mix_words(just_string):
    splitter = just_string.split(' ')
    random.shuffle(splitter)
    return ' '.join(splitter)


print letters("Trees Are So Kind")

print palindrome("avid diva")

print find_letter("Bears are the best animals ever", 'b')

print mix_words("Bears are the best animals ever")
