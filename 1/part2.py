import sys
l = [int(x) for x in sys.stdin.readlines()]
for i in range(len(l)):
    for j in range(i, len(l)):
        for k in range(j, len(l)): # I know this is slower then making all sums and doing binary search. But input is small
            if l[i] + l[j] + l[k] == 2020:
                print(l[j] * l[i] * l[k])