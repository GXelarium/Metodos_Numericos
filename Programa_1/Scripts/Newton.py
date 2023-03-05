import numpy as np
import funciones as f

def norma(vector):
    return np.absolute(vector).max()


def iter(F,op):
    return F - np.matmul(np.linalg.inv(f.jacob(F,op)),f.func(F,op))


def metodo(F,max=15,tol=0.00005,op=0):
    iteracion = iter(F,op)
    count = 0
    for i in range(max):
        aux = iteracion
        iteracion = iter(iteracion,op)
        error = norma(iteracion-aux)
        if error < tol:
            break
        count += 1
    
    print("Error: {:.6f} \nIteraciones:{}".format(error, count))
        
-Israel Jesus Velez Solano

    return iteracion


