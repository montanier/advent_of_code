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

print(forest)
best_view = 0

for i in range(1,forest.shape[0]-1):
    for j in range(1,forest.shape[1]-1):
        current = forest[i,j]

        view_up = 0
        for v_i in range(1,i+1):
            view_up += 1
            if forest[i-v_i,j] >= current:
                break

        view_down = 0
        for v_i in range(1,forest.shape[0]-i):
            view_down += 1
            if forest[i+v_i,j] >= current:
                break

        view_left = 0
        for v_j in range(1,j+1):
            view_left += 1
            if forest[i,j-v_j] >= current:
                break

        view_right = 0
        for v_j in range(1,forest.shape[1]-j):
            view_right += 1
            if forest[i,j+v_j] >= current:
                break

        view = view_up * view_down * view_left * view_right
        if view > best_view:
            best_view = view

print(best_view)
