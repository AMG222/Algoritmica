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