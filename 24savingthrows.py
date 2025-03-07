import random

# dc: 5
save = 0
trials = 0

while True:
    trials += 1
    roll = random.randint(1, 20)
    if roll >= 5: 
        save += 1
    print(save/trials)

# dc: 10 with advantage
while True:
    trials += 1
    r1 = random.randint(1, 20)
    r2 = random.randint(1, 20)
    if r1 > r2: roll = r1
    else: roll = r2
    if roll >= 10: 
        save += 1
    print(save/trials)

# dc: 15 with disadvantage
while True:
    trials += 1
    r1 = random.randint(1, 20)
    r2 = random.randint(1, 20)
    if r1 < r2: roll = r1
    else: roll = r2
    if roll >= 15: 
        save += 1
    print(save/trials)