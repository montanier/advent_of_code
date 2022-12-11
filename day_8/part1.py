import sys
import re
from typing import List

import numpy as np

forest = []

for line in open(sys.argv[1], 'r').readlines():
    line = line.rstrip()
    forest.append([int(char) for char in line])

forest = np.asarray(forest)

visible_tree = set()

for i in range(forest.shape[0]):
    row = forest[i, :]
    tallest_so_far = -1
    for coord, tree in enumerate(row):
        if tree > tallest_so_far:
            visible_tree.add((i, coord))
            tallest_so_far = tree

    tallest_so_far = -1
    for coord, tree in reversed(list(enumerate(row))):
        if tree > tallest_so_far:
            visible_tree.add((i, coord))
            tallest_so_far = tree

for j in range(forest.shape[1]):
    row = forest[:, j]
    tallest_so_far = -1
    for coord, tree in enumerate(row):
        if tree > tallest_so_far:
            visible_tree.add((coord, j))
            tallest_so_far = tree

    tallest_so_far = -1
    for coord, tree in reversed(list(enumerate(row))):
        if tree > tallest_so_far:
            visible_tree.add((coord, j))
            tallest_so_far = tree


print(len(visible_tree))

