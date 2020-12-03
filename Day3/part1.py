import sys

lines = open("input.txt", "r").read().splitlines()
x = 0
trees = 0
for l in lines:
    if l[x] == '#':
        trees += 1
    x = (x + 3) % len(l)


print(trees)