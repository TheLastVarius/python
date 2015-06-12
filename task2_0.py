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

new_root_childrens = root.childrens[::-1]
new_node_childrens = node.childrens[::-1]

new_root = []
new_root.append(root.data)

for element in new_root:
    if re.search(r'html',element):
        root.data = '<html>\n'
        root2 = TreeNode('</html>',None,0)
    elif re.search(r'head',element):
        root.data = '<head>\n'
        root2 = TreeNode('</head>',None,0)
    elif re.search(r'title',element):
        root.data = '<title>\n'
        root2 = TreeNode('</title>',None,0)

for element in new_root_childrens:
    if re.search(r'head',element):
        node = TreeNode('    </head>\n',root,1)
        root.add_child(node)
    elif re.search(r'title',element):
        node = TreeNode('    </title>\n',root,1)
        root.add_child(node)
    elif re.search(r'html',element):
        node = TreeNode('    </html>\n',root,1)
        root.add_child(node)

node.childrens = new_node_childrens[::-1]

for element in new_node_childrens:
    if re.search(r'title',element):
        node_2 = TreeNode('        </title>\n',node,2)
        node.add_child(node_2)
    elif re.search(r'html',element):
        node_2 = TreeNode('        </html>\n',node,2)
        node.add_child(node_2)
    elif re.search(r'head',element):
        node_2 = TreeNode('        </head>\n',node,2)
        node.add_child(node_2)

output = open('new_html.txt', 'w')

output.writelines('%s' %element for element in root.data)
output.writelines('%s' %element for element in root.childrens)
output.writelines('%s' %element for element in node.childrens)
output.writelines('%s' %element for element in root2.data)

output.close()

source_2 = open('new_html.txt')
output_2 = open('finaly_html.txt', 'w')

for line in source_2:
    if re.search('head\n', line):
        output_2.write(re.sub('head\n', '<head>\n', line))
    elif re.search('title\n', line):
        output_2.write(re.sub('title\n', '<title>\n', line))
    else:
        output_2.write(line)

