import sys

tot_priorities = 0
grp_cpt = 0

for line in open(sys.argv[1], 'r').readlines():
    grp_cpt += 1

    line = line.strip()
    current_set = set(line)

    if grp_cpt == 1:
        set_so_far = current_set
    else:
        set_so_far = set_so_far & current_set

    if grp_cpt == 3:
        inter = list(set_so_far)[0]

        if inter.isupper():
            priority = ord(inter) - ord('A') + 27
        else:
            priority = ord(inter) - ord('a') + 1

        tot_priorities += priority

        grp_cpt = 0
        set_so_far = set()

print(tot_priorities)

