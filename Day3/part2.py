import sys


lines = open("input.txt", "r").read().splitlines()

def tree(xm, ym):
    x = 0
    y = 0
    trees = 0
    for y in range(0, len(lines), ym):
        if lines[y][x] == '#':
            trees += 1
        x = (x + xm) % len(lines[0])
    return trees

totaltrees = 1

for l in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    totaltrees *= tree(l[0], l[1])

print(totaltrees)