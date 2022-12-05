import sys

tot_priorities = 0

for line in open(sys.argv[1], 'r').readlines():
    line = line.strip()
    tot_size = len(line)

    first_half = set(line[0:tot_size//2])
    second_half = set(line[tot_size//2:])

    inter = list(first_half & second_half)[0]
    if inter.isupper():
        priority = ord(inter) - ord('A') + 27
    else:
        priority = ord(inter) - ord('a') + 1

    tot_priorities += priority

print(tot_priorities)

