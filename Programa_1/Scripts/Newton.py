import numpy as np
import funciones as f

def norma(vector):
    return np.absolute(vector).max()


def iter(F,op):
    funcion = f.func(F,op)
    jacobiana = f.jacob(F,op)
    prod = np.matmul(np.linalg.inv(jacobiana),funcion)
    for i in range(len(F)):
        print("\t\t{:.6f}\t\t".format(F[i]),end=" ")
        for j in range(len(F)):
            print("{:.6f} ".format(jacobiana[i][j]), end=" ")
        print("\t\t{:.6f} \t\t{:6f}".format(funcion[i],prod[i]), end=" ")
        if op<3 and i!= 1:
            print("")
        elif op>2 and i!=2:
            print("")
        

    return F - prod


def metodo(F,max=15,tol=0.00005,op=0):
    iteracion = F
    print("")
    if len(F)==3:
        print("Iteración \tPunto \t\t\t\t Jacobiana \t\t\tValores de la función \t\tJ⁻1 * F \tError")
    else:
        print("Iteración \tPunto \t\t\t\t Jacobiana \t\tValores de la función \tJ-1 * F \tError")
    for i in range(1, max+1):
        print("{}".format(i), end=" ")
        aux = iteracion
        iteracion = iter(iteracion,op)
        error = norma(iteracion-aux)
        print("\t{:.6f}".format(error))
        print
        if error < tol:
            break
        print("\n")
    
    print("\n---------------\nSOLUCIÓN \nNúmero de iteracion: {} \nError: {:.6f} \nPunto encontrado: {}".format(i, error, iteracion))

    return iteracion




