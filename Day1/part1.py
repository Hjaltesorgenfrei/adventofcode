import sys
l = [int(x) for x in sys.stdin.readlines()]
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i] + l[j] == 2020:
            print(l[j] * l[i])