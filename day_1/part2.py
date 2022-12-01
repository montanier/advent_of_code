import sys


def update(max_calories, current_calories):
    index_min = min(range(len(max_calories)), key=max_calories.__getitem__)
    if current_calories > max_calories[index_min]:
        del max_calories[index_min]
        max_calories.append(current_calories)


max_calories = [0]*3
current_calories = 0

for line in open(sys.argv[1], 'r').readlines():
    if line == '\n':
        update(max_calories, current_calories)
        current_calories = 0
    else:
        current_calories += int(line)

update(max_calories, current_calories)

print(sum(max_calories))
