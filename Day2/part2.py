import sys

validcount = 0

for l in sys.stdin.readlines():
    req, password = [word.strip() for word in l.split(':')]
    reqnums, letter = req.split(" ")
    reqmin, reqmax = [int(i) - 1 for i in reqnums.split("-")]
    # print(f"{reqmin} {reqmax} {letter} -> {password}")
    if password[reqmin] == letter and password[reqmax] != letter:
        validcount += 1
    if password[reqmin] != letter and password[reqmax] == letter:
        validcount += 1

print(validcount)