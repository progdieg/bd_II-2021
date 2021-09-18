import math

def funcion(x):
    suma=0
    for n in range(0,50):
        suma += math.pow(x, n) / math.factorial(n)
    return suma

print("resultado de la funcion exponencial",funcion(2))
print("resultado de la funcion math.exp",math.exp(funcion(2)))
