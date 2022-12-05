import sys

cpt_free_elf = 0

for line in open(sys.argv[1], 'r').readlines():
    line = line.strip()
    first_elf, second_elf = line.split(',')

    min_first_elf, max_first_elf = [int(x) for x in first_elf.split('-')]
    min_second_elf, max_second_elf = [int(x) for x  in second_elf.split('-')]

    if not (max_first_elf < min_second_elf) and not(max_second_elf < min_first_elf):
        cpt_free_elf += 1

print(cpt_free_elf)
