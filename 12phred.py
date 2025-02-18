import math

# class example: going from prob to char
p = 1 * 10 ** -3.2
pqv = -int(math.log10(p) * 10)
symbol = chr(pqv + 33)
print(symbol)

# class example: going from char to prob
c = 'A'
pqv = ord(c) - 33
print(10 ** (-pqv/10))

# character to probability function
def char_to_prob(c):
    pqv = ord(c) - 33
    return (10 ** (-pqv / 10)) 

print(char_to_prob('A'))
print(char_to_prob('B'))
print(char_to_prob('='))

# probability to character function
def prob_to_char(p):
    if p > 1: return None
    if p <= 0: return None
    pqv = -int(math.log10(p) * 10)
    symbol = chr(pqv + 33)
    return symbol

print(prob_to_char(0.001))
print(prob_to_char(0.0005))
print(prob_to_char(0))
print(prob_to_char(1))