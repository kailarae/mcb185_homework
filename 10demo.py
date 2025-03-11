# 10demo.py by kaila_donato

import math

print("hello, again") # greeting

print(1.5e-2)

# math operators
print(5//2)
print(2.5e-3 / 5)
print(5 * (2+1))

# math functions
math.factorial(3)

# variables
a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)

# type
print(type(a), type(b), type (c))

print(type(a), type(b), type(c), sep=', ', end='!\n') # puts a comma followed by a space between print values
                                                      # \n means "newline," creates a vertical space

print(type(a), type(b), type(c), sep='\t') # separate print values with tab

# functions
def pythagoras(a, b):
        c = math.sqrt(a**2 + b**2)
        return c
hyp = pythagoras(3, 4)
print(hyp)

def pythagoras(a, b):
        return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

# block structure
def pythagoras(a, b): return math.sqrt(a**2 + b**2)

# practice
def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h): return (w * h) / 2

# strings
s = 'hello world'
print(s, type(s))

# conditionals 
a = 2
b = 2
if a == b:
        print('a equals b')
print (a, b)

def is_even(x):
        if x % 2 == 0: return True
        return False

print(is_even(2))
print(is_even(3))

# Boolean
c = a == b
print(c)
print(type(c))

# if-elif-else
a = 5
b = 7
if a < b:
        print('a < b')
elif a > b:
        print('a > b')
else:
        print('a == b')

if a < b: print('a < b')
elif a <= b: print('a <= b')
else: print('this will never print!')

# chaining