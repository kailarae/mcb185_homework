import random

trials = 0
revive = 0
stabilize = 0
die = 0

n = 10000000
for i in range(n):
    saves = 0
    fails = 0
    while True:
        roll = random.randint(1,20)
        if roll == 1: fails += 2
        elif roll < 10: fails += 1 
        elif roll == 20: 
            revive += 1
            break
        else: saves += 1
        if fails >= 3: 
            die += 1
            break
        if saves >= 3:
            stabilize += 1
            break

print(die/n, stabilize/n, revive/n)