import sys
from pprint import pprint
from dataclasses import dataclass

@dataclass
class Monkey:
    items: list
    op_1: str
    op_2: str
    test_op: None
    test: int
    if_true: int
    if_false: int

monkeys = {}
tracker = {}

cycle_length = 1

def round(monkeys):
    for uid, monkey in monkeys.items():
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            if "old" in monkey.op_2:
                op_2 = item
            else:
                op_2 = int(monkey.op_2)
            worry = monkey.test_op(item, op_2)
            worry = worry % cycle_length
            if worry % monkey.test == 0:
                monkeys[monkey.if_true].items.append(worry)
            else:
                monkeys[monkey.if_false].items.append(worry)
            tracker[uid] += 1

def print_status(monkeys):
    for uid, monkey in monkeys.items():
        print(f"{uid}: {monkey.items}")


for line in open(sys.argv[1], 'r').readlines():
    line = line.rstrip()

    if "Monkey" in line:
        _, current_monkey = line.split(" ")
        current_monkey = int(current_monkey[:-1])
    elif "Starting items" in line:
        _, list_pass = line.split(":")
        list_pass = list_pass.split(",")
        list_pass = [int(monkey) for monkey in list_pass]
    elif "Operation" in line:
        _, ope = line.split(":")
        _, ope = ope.split("=")
        if "+" in ope:
            op_1, op_2 = ope.split("+")
            test_op = lambda x, y: x + y
        if "*" in ope:
            op_1, op_2 = ope.split("*")
            test_op = lambda x, y: x * y
    elif "Test" in line:
        _, test = line.split(":")
        _, _, _, nb = test.split(" ")
        test = int(nb)
        cycle_length = cycle_length * test
    elif "If true" in line:
        _, throw = line.lstrip().split(":")
        _, _, _, _, throw = throw.split(" ")
        if_true = int(throw)
    elif "If false" in line:
        _, throw = line.lstrip().split(":")
        _, _, _, _, throw = throw.split(" ")
        if_false = int(throw)
    else:
        monkeys[current_monkey] = Monkey(
            items=list_pass,
            op_1=op_1,
            op_2=op_2,
            test_op=test_op,
            test=test,
            if_true=if_true,
            if_false=if_false
        )
        tracker[current_monkey] = 0

monkeys[current_monkey] = Monkey(
    items=list_pass,
    op_1=op_1,
    op_2=op_2,
    test_op=test_op,
    test=test,
    if_true=if_true,
    if_false=if_false
)
tracker[current_monkey] = 0

print_status(monkeys)

for round_id in range(10000):
    round(monkeys)

print(tracker)
