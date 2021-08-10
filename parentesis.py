def cadena_parentesis(parentesis):
    pila = []
    parentesis = {'(': ')', '[': ']'}
    cadena = []
    for c in cadena:
        if c in parentesis:
            pila.append(c)
        elif len(pila) == 0 or c != parentesis[pila.pop]:
            return False
    return len(pila)== 0

print(cadena_parentesis(')['))