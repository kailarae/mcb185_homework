import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0
for i in range(trials):
    classroom = []
    for i in range(people):
        bday = random.randint(0, days)
        if bday in classroom:
            shared += 1
            break     
        classroom.append(bday)
print(shared / trials)

# generate a classroom (people)
# generate a bday for every person
# check to see if bdays are the same 