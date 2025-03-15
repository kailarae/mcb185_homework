import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0
for i in range(0, trials):
    calendar= []
    # adding all days to the calendar
    for i in range(0, days):
        calendar.append(0)
    # identifying birthdays
    for j in range(people):
        bday = random.randint(0, 364) # needs to be one less because the list length is 365, but the first index is 0
        calendar[bday] += 1
        # need to identify if any value is 2
        if 2 in calendar:
            shared += 1
            break
print(shared / trials)