import sys
import re
from typing import List

class Node:
    name: str
    size: int
    is_dir: bool
    children: List
    parent: 'Node'

    def __str__(self):
        return(f"{self.name} ({self.size}) {self.is_dir}")

file_pattern = re.compile("([0-9]+) ([a-zA-Z\.]+)")

def print_tree(current, indent):
    print("".join([" "]*indent) + str(current))
    for child in current.children:
        print_tree(child, indent+2)

def update_size(current):
    size = current.size
    for child in current.children:
        size += update_size(child)
    current.size = size
    return size

def find_dir_lower_than(current, threshold):
    result = []
    if current.size < threshold and current.is_dir == True:
        result.append(current)
    for child in current.children:
        result += find_dir_lower_than(child, threshold)
    return result


root = Node()
root.name = "/"
root.is_dir = True
root.children = []
root.parent = None
root.size = 0

current = root
is_listing = False

for line in open(sys.argv[1], 'r').readlines():
    line = line.rstrip()

    if line == "$ ls":
        is_listing = True

    elif "$ cd" in line and ".." not in line:
        is_listing == False
        new_node = Node()
        _, _, name = line.split(" ")
        new_node.name = name
        new_node.is_dir = True
        new_node.children = []
        new_node.parent = current
        new_node.size = 0

        current.children.append(new_node)

        current = new_node
    elif line == "$ cd ..":
        current = current.parent
        is_listing == False

    elif is_listing == True:
        file_match = file_pattern.match(line)
        if file_match:
            new_node = Node()
            new_node.name = file_match.group(2)
            new_node.size = int(file_match.group(1))
            new_node.is_dir = False
            new_node.children = []
            new_node.parent = current

            current.children.append(new_node)

# print_tree(root, 0)

update_size(root)

# print_tree(root, 0)

result = find_dir_lower_than(root, 100000)
sum_res = 0
for res in result:
    sum_res += res.size
print(sum_res)
