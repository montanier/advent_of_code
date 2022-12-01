import sys

max_calories = 0
current_calories = 0

for line in open(sys.argv[1], 'r').readlines():
    if line == '\n':
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(line)

print(max_calories)
