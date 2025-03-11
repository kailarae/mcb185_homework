# tuples: collection of values separated by a comma
t = 1, 2
print(t)
print(type(t))

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, x2, y1, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y1

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4) # unpacking the tuple
print(mx, my)
print(type(mx))

print(m[0], m[1])             # uses numeric index to unpack tuple

# iteration
i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)

# for i in range()
for i in range(1, 10, 3):     # initial value, end-before limit, increment
    print(i)

for i in range(0, 5):         # can skip intitial value if 1 
    print(i)

# for items in containers
basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)

for i in range(len(basket)):  # len returns the number of items in basket
    print(basket[i])

# nesting
for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')

# random number generators
import random 

for i in range(5):
    print(random.random())

# practice problems

# triangular
def triangular(n):
    tri = 0             # variable to hold the sum
    for i in range(1, n+1):
        tri = tri + i
    return tri

print(triangular(8))

# factorials
def factorial(n):
    if n == 0: return 1
    fac = 1
    for i in range(1, n+1):
        fac = fac * i 
    return fac

print(factorial(5))
print(factorial(10-5))

# poisson
import math
def poisson(n, k):
    fac = 1
    for i in range(1, k+1):
        fac = fac * i
    return n ** k * math.e ** (-n / fac)

print(poisson(1, 3))

# n choose k
def nchoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print(nchoosek(4, 5))

# euler
def euler(limit):
    e = 0
    for n in range(limit):
        e = e + 1 / factorial(n)
    return e

print(euler(100)) 

# prime number
def prime(n):
    for den in range(2, n//2 + 1):
        if n % den == 0: return False
    return True

print(prime(7))

# estimate pi using nilakantha series
def nilakantha(limit):
    pi = 3
    for i in range(1, limit+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi

print(nilakantha(10))

fib1 = 0
fib2 = 1
print(fib1)
for i in range(1, 10):
    fibt = fib1 + fib2 
    fib1 = fib2 
    fib2 = fibt
    print(fib1)
