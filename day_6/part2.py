import sys

for line in open(sys.argv[1], 'r').readlines():
    line = line.rstrip()

    for start in range(0,len(line)-14):
        buff = line[start:start+14]
        if len(set(buff)) == 14:
            print(start+14)
            break
