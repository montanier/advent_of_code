import sys

for line in open(sys.argv[1], 'r').readlines():
    line = line.rstrip()

    for start in range(0,len(line)-4):
        buff = line[start:start+4]
        if len(set(buff)) == 4:
            print(start+4)
            break
