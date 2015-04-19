#!/usr/bin/ipython


def repetitive(catalog):
    result = []
    for element in catalog:
        if catalog.count(element) > 1 and element not in result:
            result.append (element)
    return ' и '.join(['{}'.format(res) for res in result])


def statistic(catalog):
    type_catalog = [element.__class__.__name__ for element in catalog]
    set_catalog = set(type_catalog)
    dict_catalog = {set_element: type_catalog.count(set_element) for set_element in set_catalog}
    return ', '.join(['{0} => {1}'.format(value,key) for value, key in dict_catalog.iteritems()])


def sorting(catalog):
    return sorted(catalog, key = lambda input:input[-1])


def ins_sort(catalog, line):
    start = 0
    end = len(catalog) - 1
    while start < end:
        middle = int((start + end) / 2)
        if line > catalog[middle]:
            start = middle + 1
        else:
            end = middle
    if catalog[end] < line:
        catalog.insert(end + 1, line)
    else:
        catalog.insert(end, line)
    return catalog    


def sort_ins(catalog1, catalog2, letter):
    start = 0
    end = len(catalog1) - 1
    while start < end:
        middle = int((start + end) / 2)
        if letter > catalog1[middle]:
            start = middle + 1
        else:
            end = middle
    if catalog1[end] == letter:
        catalog2.insert(end, letter)
    else:
        return 'Элемент не найден'
    return catalog2


def find_del(line):
    splitter = line.split()
    for element in splitter:
        if len(element) % 2 != 0:
            splitter.remove(element)
    return ' '.join(splitter)


def sequence(catalog):
    index = 0
    catalog_line = []
    catalog_len = []
    while index < len(catalog) - 1:
        line = [catalog[index]]
        while catalog[index] + 1 == catalog[index + 1]:
            line.append(catalog[index + 1])
            index += 1
            if index == len(catalog) - 1:
                break
        index += 1
        catalog_line.append(line)
    for element in catalog_line:
        catalog_len.append(len(element))
    catalog_len_enum = list(enumerate(catalog_len))
    return ' '.join(['{}'.format(catalog_line[element[0]]) for element in catalog_len_enum if element[1] == max(catalog_len)])        


print repetitive([1,2,3,2,1,'a','b','ab','abc','ba','abc'])

print statistic([1, 2, 'abc',[1,2,3], 1.5])

print sorting(['a','abc','cda'])

print ins_sort(['a','cda','dea'], 'cca')

print sort_ins(['a','cda','dea'], ['ab', 'cba', 'efg'], 'cda')

print find_del('Hello my pretty world!')

print sequence([1,2,3,5,6,7,8,10,11,12,13])