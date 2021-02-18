import numpy

def levenstein(x, y):
    lx = len(x)
    ly = len(y)
    D = numpy.zeros(shape = (ly + 1, lx + 1))
    D[0, 0] = 0
    for i in range(1, ly + 1):
        D[i, 0] = i
    for j in range(1, lx + 1):
        D[0, j] = j
    for j in range(1, lx + 1):
        for i in range(1, ly + 1):
            D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i - 1, j - 1] + int(x[j - 1] != y[i - 1]))
    return D[ly, lx]

def levenstein_damerau_rest(x, y):
    lx = len(x)
    ly = len(y)
    D = numpy.zeros(shape = (ly + 1, lx + 1))
    D[0, 0] = 0
    for i in range(1, ly + 1):
        D[i, 0] = i 
    for j in range(1, lx + 1):
        D[0, j] = j
    for j in range(1, lx + 1):
        for i in range(1, ly + 1):
            D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i - 1, j - 1] + int(x[j - 1] != y[i - 1]))
            if (i and j > 1) and (x[j - 2] == y[i - 1] and x[j - 1] == y[i - 2]):
              D[i, j] = min(D[i, j], D[i - 2, j - 2] + 1)              
    return D[ly, lx]

def levenstein_damerau_intermedia(x, y):
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
          D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i - 1, j - 1] + int(x[i - 1] != y[j - 1]))
          if (i and j > 1) and (x[i - 2] == y[j - 1] and x[i - 1] == y[j - 2]):
            D[i, j] = min(D[i, j], D[i - 2, j - 2] + 1) 

          if (i > 2 and j > 1) and (x[i - 3] == y[j - 1] and x[i - 1] == y[j - 2]):
            D[i, j] = min(D[i, j], D[i - 3, j - 2] + 2) 
          if (i > 1 and j > 2) and ((x[i - 1] == y[j - 3] and x[i - 2] == y[j - 1])):
            D[i, j] = min(D[i, j], D[i - 2, j - 3] + 2)  

  return D[lx, ly]
  
def langford_directo(N, allsolutions): 
  N2 =2*N
  seq = [0]*N2
  def backtracking(num):
    if num<=0: # ¿La solución es completa?
      yield "-".join(map(str, seq)) 
    else: # Si no es completa
      for i,j in zip(range(N2 - num), range(num + 1, N2)):
        if seq[i] == 0 and seq[j] == 0: # ¿La solución es prometedora?
          seq[i] = num
          seq[j] = num
          for s in backtracking(num - 1):
            yield s
        else:
          continue
        seq[i] = 0
        seq[j] = 0

  if N%4 not in (0,3):
    yield "no hay solucion"
  else:
    count = 0
    for s in backtracking(N): 
      count += 1
      yield "solution %04d -> %s" % (count,s) 
      if not allsolutions:
        break