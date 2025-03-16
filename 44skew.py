import sequence

#count gc content in the initial window
#scroll across the rest of the nt and add as you come across

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10                              # window size
g = 0                               # g count
c = 0                               # c count
for i in range(len(seq) - w + 1):
    s = seq[i:i+w]                  # window
    if i == 0: 
        g = s.count('G')
        c = s.count('C')
    else:
        # removing left most nt
        if seq[i-1] == 'G':
            g -= 1
        if seq[i-1] == 'C':
            c -= 1
        # adding right most nt
        if seq[i + w - 1] == 'G':
            g += 1
        if seq[i + w - 1] == 'C':
            c += 1
    print(i, sequence.gc_comp(s), sequence.gc_skew(s))