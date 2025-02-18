# for oligos <= 13 nt
def tm(g, c, a, t): return (a + t) * 2 + (g + c) * 4
print(tm(2, 3, 2, 5))

# for longer oligos
def tm(g, c, a, t): return 64.9 + 41 * (g + c - 16.4) / (g + c + a + t)
print(tm(5, 7, 3, 4))

# class example
def tm(a, c, g, t):
    length = a + c + g + t
    if length <= 13: return (a + t) * 2 + (g + c) * 4
    return 64.9 + 41 * (g + c - 16.4) / length

print('oligo1: ', tm(5, 3, 0, 2))
print('oligo2: ', tm(5, 3, 4, 2))
print('oligo3: ', tm(6, 7, 8, 9))