import numpy

def levenstein(x, y):
    lx = len(x)
    ly = len(y)
    D = numpy.zeros(shape = (lx + 1, ly + 1))
    D[0, 0] = 0
    for i in range(1, lx + 1):
        D[i, 0] = i
    for j in range(1, ly + 1):
        D[0, j] = j
    for i in range(1, lx + 1):
        for j in range(1, ly + 1):
            D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i - 1, j - 1] + int(x[i + 1] != y[j + 1]))
    return D[lx + 1, ly + 1]

"""
Compute the Damerau-Levenshtein distance between two given
strings (x and y)
"""
def damerau_levenshtein_distance(x, y):
    d = {}
    lx = len(x)
    ly = len(y)
    for i in range(-1,lx+1):
        d[(i,-1)] = i+1
    for j in range(-1,ly+1):
        d[(-1,j)] = j+1

    for i in range(lx):
        for j in range(ly):
            if x[i] == y[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and x[i]==y[j-1] and x[i-1] == y[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

    return d[lx-1,ly-1]