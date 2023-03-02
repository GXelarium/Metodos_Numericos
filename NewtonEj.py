import numpy as np
import math 

def func(F):
    x = F[0]
    y = F[1]
    return np.array([1 - x**2 - x + y**2,
                     y - math.sin(x**2)])


def jacob(F):
    x = F[0]
    y = F[1]
    return np.array([[-2*x-1, 2*y],
                     [-2*x*math.cos(x**2), 1]])


def norma(vector):
    return np.absolute(vector),max()


def iter(F):
    return F - np.matmul(np.linalg.inv(jacob(F)),func(F))


def Newton(x,y,max=15,tol=0.00005):
    F = np.array([x,y])
    iteracion = iter(F)
    
    for i in range(max):
        iteracion = iter(iteracion)
    
    print(iteracion)


if __name__ == '__main__':
    Newton(0.5,0.5,3)