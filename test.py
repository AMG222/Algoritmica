def is_complete(s): #Devuelve cierto sii s es un estado completo

def is_feasible(s): #Devuelve cierto sii es ya la solucion

def is_promising(s): #Devuelve falso sii es imposible que s contenga una solución factible

def branch(s): #Devuelve una secuencia de estados (que puede ser vacía) obtenidos por ramificación de s




def backtracking(s): #Explora el subárbol que tiene por raíz a s y devuelve la primera solución factible que encuentra (si la hay). Si no hay ninguna, devuelve None.
    if is_complete(s):
        if is_feasible(s):
            return s
    else:
    for s0 in branch(s):
        if is_promising(s0):
            found = backtracking(s0)
            if found != None: 
                return found
    return None
def solve (s):
    return backtracking([])


def backtracking(s, solutions): #Explora el subárbol que tiene por raíz a s y generatodas las soluciones factibles que encuentra (si las hay)
    if is_complete(s):
        if is_feasible(s):
            solutions.append(s)
    else:
        for s0 in branch(s):
            if is_promising(s0):
                backtracking(s0):
def solve (s):
    solutions = []
    backtracking([], solutions)

Recursivo
    P[j]=min o max {P[x] (+-*/) c(x,j)}
    x alternativas

Iterativo
    caso trivial
    recorrer la matriz o vector y rellenar con la op recursivo

