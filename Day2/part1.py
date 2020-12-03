import sys

validcount = 0

for l in sys.stdin.readlines():
    req, password = [word.strip() for word in l.split(':')]
    reqnums, letter = req.split(" ")
    reqmin, reqmax = [int(i) for i in reqnums.split("-")]
    # print(f"{reqmin} {reqmax} {letter} -> {password}")
    if reqmin <= password.count(letter) <= reqmax:
        validcount += 1

print(validcount)