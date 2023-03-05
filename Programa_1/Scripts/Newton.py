import numpy as np
import funciones as f

def norma(vector):
    return np.absolute(vector).max()


def iter(F,op):
    return F - np.matmul(np.linalg.inv(f.jacob(F,op)),f.func(F,op))


def metodo(F,max=15,tol=0.00005,op=0):
    iteracion = F
    print("Iteración {}: {}".format(0, iteracion))
    for i in range(1, max+1):
        jacobiana = f.jacob(iteracion,op)
        valores_funcion = f.func(iteracion,op)
        aux = iteracion
        iteracion = iter(iteracion,op)
        error = norma(iteracion-aux)
        print("Iteración {}: {}, Jacobiana: {}, Función: {}, Método: {}".format(i, iteracion, jacobiana, valores_funcion, error))
        if error < tol:
            break
    
    print("Error: {:.6f} \nIteraciones:{}".format(error, i))

    return iteracion


