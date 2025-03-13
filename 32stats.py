import sys

# converting numbers in command line to floats
numbers = []
for arg in sys.argv[1:]:
    f = float(arg)
    numbers.append(f)

# minmax
def  minmax(numbers):
    mini = numbers[0]
    maxi = numbers[0]
    for number in numbers[1:]:
         if number < mini: mini = number
         if number > maxi: maxi = number
    return mini, maxi
m1, m2 = (minmax(numbers))

# mean
def avglist(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

# standard deviation
def stdev(numbers):
    diff = 0
    for number in numbers[::]:
        diff += (number - avglist(numbers)) ** 2
    return (diff / len(numbers) - 1) ** 0.5

# median value
numbers.sort()                  # need to sort in numerical order
def medians(numbers):
    middle = len(numbers) / 2
    center = int(middle)
    # for when the length is odd
    if len(numbers) % 2 == 1:
        return numbers[center]           # converting to integer
    # for when length is even
    else: 
        m = (numbers[center] + numbers[center - 1]) / 2
        return m

# formatting output 
print('number of values:', len(numbers))
print('minimum:', m1)
print('maximum:', m2)
print('mean:', avglist(numbers))
print('standard deviation:', f'{stdev(numbers):.4f}')
print('median:', medians(numbers))