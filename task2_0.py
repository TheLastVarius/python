#!/usr/bin/python
#coding=utf-8

import re

class TreeNode:
    def __init__(self, data=None, parent=None, level=None):
        self.data = data
        self.parent = parent
        self.level = level
        self.childrens = []

    def __str__(self):
        return str(self.data)

    def add_child(self, child):
        self.childrens.append(child.data)

source = open('html.txt')

spaces = 0
levels = 0

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

new_root_childrens = []
new_node_childrens = []

root_catalog = []
root_catalog.append(root.data)
new_root = []

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

output = open('new_html.txt', 'w')

output.writelines('%s' %element for element in new_root)
output.writelines('%s' %element for element in new_root_childrens)
output.writelines('%s' %element for element in new_node_childrens)

output.close()

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