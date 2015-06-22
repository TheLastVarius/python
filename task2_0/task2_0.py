#!/usr/bin/python
#coding=utf-8

import re

class TreeNode:
    def __init__(self, data=None, parent=None, level=None):
        self.data = data #данные
        self.parent = parent #родитель
        self.level = level #уровень вложенности, определяемый количеством пробелов перед текстом
        self.childrens = [] #список детей

    def __str__(self):
        return str(self.data)

#метод, добавляющий ребенка в список детей родителя
    def add_child(self, child):
        self.childrens.append(child.data)

spaces = 0
new_root_childrens = []
new_node_childrens = []
new_root = []
root_catalog = []


try:
    source = open('html.txt', 'r')
except(FileNotFoundError):
    print 'Ошибка. Файла не существует.'
#создаем дерево, проходя построчно по файлу.
for line in source:
    compare = re.match(r' *', line)
    if compare.end() == 0:
        level = 0
        root = TreeNode(line,None,level)
    elif compare.end() - spaces == 4:
        level += 1
        if level == 1:    
            node = TreeNode(line,root,level)
            root.add_child(node)
            spaces = compare.end()
        elif level == 2:
            node_2 = TreeNode(line,node,level)
            node.add_child(node_2)
            spaces = compare.end()
    elif compare.end() - spaces == 0:
        if level == 1:    
            node = TreeNode(line,root,level)
            root.add_child(node)
        elif level == 2:
            node_2 = TreeNode(line,node,level)
            node.add_child(node_2)
source.close()

#приводим корень дерева к списку, для единообразия и удобства работы.
root_catalog.append(root.data)

#заменяем наши теги, открывающими тегами html.
#столь большое количество кода - на случай, если кто-то, будучи в такой же горячке как и я, когда писал этот код,
#решит поменять местами теги и в начало файла засунет, например title вместо html.
for element in node.childrens:
    if re.search('html', element):
        new_node_childrens.append(element.replace('html','<html>'))
    elif re.search('head', element):
        new_node_childrens.append(element.replace('head','<head>'))
    elif re.search('title', element):
        new_node_childrens.append(element.replace('title','<title>'))
    else:
        new_node_childrens.append(element)

for element in root.childrens:
    if re.search('html', element):
        new_root_childrens.append(element.replace('html','<html>'))
    elif re.search('head', element):
        new_root_childrens.append(element.replace('head','<head>'))
    elif re.search('title', element):
        new_root_childrens.append(element.replace('title','<title>'))
    else:
        new_root_childrens.append(element)

for element in root_catalog:
    if re.search('html', element):
        new_root.append(element.replace('html','<html>'))
    elif re.search('head', element):
        new_root.append(element.replace('head','<head>'))
    elif re.search('title', element):
        new_root.append(element.replace('title','<title>'))
    else:
        new_root.append(element)

#записываем открывающие теги в новый txt файл.
output = open('new_html.txt', 'w')

output.writelines('%s' %element for element in new_root)
output.writelines('%s' %element for element in new_root_childrens)
output.writelines('%s' %element for element in new_node_childrens)

output.close()

#дозаписываем в новый txt файл закрывающие теги.
output_2 = open('new_html.txt', 'a')

for element in node.childrens:
    if re.search('html', element):
        output_2.writelines(element.replace('html','</html>'))
    if re.search('head', element):
        output_2.writelines(element.replace('head','</head>'))
    if re.search('title', element):
        output_2.writelines(element.replace('title','</title>'))

for element in root.childrens:
    if re.search('html', element):
        output_2.writelines(element.replace('html','</html>'))
    if re.search('head', element):
        output_2.writelines(element.replace('head','</head>'))
    if re.search('title', element):
        output_2.writelines(element.replace('title','</title>'))

for element in root_catalog:
    if re.search('html', element):
        output_2.writelines(element.replace('html','</html>'))
    if re.search('head', element):
        output_2.writelines(element.replace('head','</head>'))
    if re.search('title', element):
        output_2.writelines(element.replace('title','</title>'))

output_2.close()