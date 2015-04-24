#!/usr/bin/python


def key_zero(dictionary, line):
    if line not in dictionary.keys():
        return 'Нет такого ключа'
    else:
        dictionary[line] = None
        return dictionary


def stuck_dict(dictionary1, dictionary2):
    for element in dictionary1.keys():
        if element in dictionary2.keys():
            del dictionary1[element]
            del dictionary2[element]
    return dict(dictionary1.items()+dictionary2.items())


def calculate(procedure, arg1, arg2):
    oper = {'add' : arg1+arg2, 'deduct' : arg1-arg2, 'multiply' : arg1*arg2, 'divided' : arg1/arg2}
    return oper[procedure]


def swap(dictionary):
    return dict(zip(dictionary.values(),dictionary.keys()))


print key_zero({'Nik' : 4128, 'Dmitry' : 4093, 'Din' : 4039}, 'Dik')

print stuck_dict({'Nik' : 4128, 'Dmitry' : 4093, 'Din' : 4039}, {'Nik' : 4128, 'Dima' : 4093, 'Dinara' : 4039})

print calculate('add', 2, 4)

print swap({'Nik' : 4128, 'Dmitry' : 4093, 'Din' : 4039})    