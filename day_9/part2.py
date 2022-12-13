from dataclasses import dataclass, astuple
import re
import sys
from typing import List

import numpy as np

@dataclass
class Pos:
    x: int = 0
    y: int = 0

def update_nodes(nodes):

    for node_id in range(1,len(nodes)):
        current = nodes[node_id]
        nxt = nodes[node_id - 1]
        if abs(current.y - nxt.y) <= 1 and abs(current.x - nxt.x) <= 1:
            continue
        else:
            delta_x = nxt.x - current.x
            delta_x = max(-1, delta_x)
            delta_x = min(1, delta_x)
            delta_y = nxt.y - current.y
            delta_y = max(-1, delta_y)
            delta_y = min(1, delta_y)

            current.x += delta_x
            current.y += delta_y




if __name__ == "__main__":
    visited = set()

    nodes = []
    for i in range(10):
        nodes.append(Pos(0,0))

    visited.add(astuple(nodes[-1]))

    for line in open(sys.argv[1], 'r').readlines():
        line = line.rstrip()
        move, length = line.split(" ")
        length = int(length)

        while length > 0:
            length -= 1

            if move == "R":
                nodes[0].x += 1
            elif move == "L":
                nodes[0].x -= 1
            elif move == "D":
                nodes[0].y -= 1
            elif move == "U":
                nodes[0].y += 1

            update_nodes(nodes)
            visited.add(astuple(nodes[-1]))

    print(len(visited))
