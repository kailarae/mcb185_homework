import math
import sys

# calculating valid probabilities
probs = []
for arg in sys.argv[1:]:
    f = float(arg)
    if f >= 1 or f <= 0: 
        sys.exit('error: not a probability')
    probs.append(f)

# ensuring probabilities add to 1.0
total = 0
for prob in probs[::]:
    total += prob
if not math.isclose(total, 1.0):
    sys.exit('error: probability must sum to 1.0')
    
# calculating entropy
h = 0
for p in probs:
    h -= p * math.log2(p)

print(f'{h:.4f}')           # prints f-string of h with 4 decimal points