import random
import sys
import math

triples = []

for a in range(1, 100):
    for b in range(a, 100):
        c = (a**2 + b**2) ** 0.5
        if c % 1 == 0: 
            if a < b: triples.append((a, b, c))

print(triples)