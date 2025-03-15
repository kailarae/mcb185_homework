import sys

alphabet = sys.argv[1]
matches = sys.argv[2]
mismatch = sys.argv[3] 

# print header
print('   ', end=' ')
for nt in alphabet:
    print(nt, end='   ')
print('')

for i in range(0, len(alphabet)):
    print(alphabet[i], end='  ')
    for j in range(0, len(alphabet)):
        if i == j: 
            print(matches, end='  ')
        else: print(mismatch, end='  ')
    print('')