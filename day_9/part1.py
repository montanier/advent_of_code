from dataclasses import dataclass, astuple
import re
import sys
from typing import List

import numpy as np

@dataclass
class Pos:
    x: int = 0
    y: int = 0

def update_tail(tail_pos, head_pos):
    if abs(head_pos.y - tail_pos.y) <= 1 and abs(head_pos.x - tail_pos.x) <= 1:
        return
    else:
        delta_x = head_pos.x - tail_pos.x
        delta_x = max(-1, delta_x)
        delta_x = min(1, delta_x)
        delta_y = head_pos.y - tail_pos.y
        delta_y = max(-1, delta_y)
        delta_y = min(1, delta_y)

        tail_pos.x += delta_x
        tail_pos.y += delta_y




if __name__ == "__main__":
    visited = set()

    head_pos = Pos(0,0)
    tail_pos = Pos(0,0)

    visited.add(astuple(tail_pos))

    for line in open(sys.argv[1], 'r').readlines():
        line = line.rstrip()
        move, length = line.split(" ")
        length = int(length)

        while length > 0:
            length -= 1
            
            if move == "R":
                head_pos.x += 1
            elif move == "L":
                head_pos.x -= 1
            elif move == "D":
                head_pos.y -= 1
            elif move == "U":
                head_pos.y += 1

            update_tail(tail_pos, head_pos)
            visited.add(astuple(tail_pos))

    print(len(visited))
