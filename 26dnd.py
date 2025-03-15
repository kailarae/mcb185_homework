import random

# average of many 3d6 rolls
trials = 0
avg = 0

while True:
    trials += 1
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    rtot = r1 + r2 + r3
    avg += rtot
    print(avg/trials)


# 3d6r1: roll 3 six-sided dice, but reroll any 1s
trials = 0
avg = 0

while True:
    trials += 1
    r1 = random.randint(1,6)
    if r1 == 1: r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    if r2 == 1: r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    if r3 == 1: r3 = random.randint(1,6)
    rtot = r1 + r2 + r3
    avg += rtot
    print(avg/trials)

# 3d6x2: roll pairs of six-sided dice 3 times, taking the maximum each time
trials = 0
avgtot = 0

while True:
    trials += 1
    # first pair
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    if r1 > r2: a = r1
    else: a = r2
    # second pair
    r3 = random.randint(1, 6)
    r4 = random.randint(1, 6)
    if r3 > r4: b = r3
    else: b = r4
    # third pair
    r5 = random.randint(1, 6)
    r6 = random.randint(1, 6)
    if r5 > r6: c = r1
    else: c = r6
    # calculating avg
    avg = a + b + c
    avgtot += avg
    print(avgtot/trials)

# 4d6d1: roll 4 six-sided dice, dropping the lowest dice roll
trials = 0
avg = 0

while True:
    trials += 1
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    r3 = random.randint(1, 6)
    r4 = random.randint(1, 6)
    # calculating lowest roll
    x = r1
    if r2 < x: x = r2
    if r3 < x: x = r3 
    if r4 < x: x = r4
    # calculating average
    tot = r1 + r2 + r3 + r4 - x
    avg += tot
    print(avg/trials)