import numpy as np
import funciones as f

def norma(vector):
    return np.absolute(vector).max()


def iter(F,op):
    return F - np.matmul(np.linalg.inv(f.jacob(F,op)),f.func(F,op))


def metodo(F,max=15,tol=0.00005,op=0):
    iteracion = F
    print("{:<10}{:<50}{:<50}{:<50}{:<50}".format("Iteracion", "Punto", "Jacobiana", "Valores de la funcion", "Resultado del metodo"))
    print("{:<10}{:<50}{:<50}{:<50}{:<50}".format(0, iteracion, f.jacob(iteracion,op), f.func(iteracion,op), iteracion))
    for i in range(1, max+1):
        aux = iteracion
        iteracion = iter(iteracion,op)
        error = norma(iteracion-aux)
        print("{:<10}{:<50}{:<50}{:<50}{:<50}".format(i, iteracion, f.jacob(iteracion,op), f.func(iteracion,op), iteracion))
        if error < tol:
            break
    
    print("\n{:<10}{:<50}{:<50}".format("Error:", error, "Iteraciones: {}".format(i)))

    return iteracion



