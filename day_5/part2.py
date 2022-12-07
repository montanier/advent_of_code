import sys

MAX_CRATES = 10

crates = {}
for i in range(1, MAX_CRATES):
    crates[i] = []

moves = []


for line in open(sys.argv[1], 'r').readlines():
    line = line.rstrip()
    char_id = 0
    next_is_crate = False

    if "move" in line:
        _, nb_moves, _, src, _, dst = line.split(' ')
        moves.append((int(nb_moves), int(src), int(dst)))

    else:
        for char in line:
            if char == "[":
                next_is_crate = True
            elif next_is_crate == True:
                next_is_crate = False
                crate_id = ((char_id - 1) / 4) + 1
                crates[crate_id].insert(0, char)

            char_id += 1


for nb_moves, src, dst in moves:
    to_move = crates[src][-nb_moves:]
    del crates[src][-nb_moves:]
    crates[dst] += to_move


res = []
for stack in crates.values():
    res.append(stack[-1])

print("".join(res))

