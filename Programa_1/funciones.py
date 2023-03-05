import numpy as np
import math 

def func(F,op):
    x = F[0]
    y = F[1]

    if op==1:
        return np.array([x**2 + x*y - 10,
                        y + 3*x*y**2 - 50])
    
    elif op==2:
        return np.array([x**2 + y**2 -9,
                         -math.e**x - 2*y - 3])

    elif op==3 or op==4:
        z = F[2]

        if op==3:
            return np.array([2*x**2 - 4*x + y**2 + 3*z**2 + 6*z + 2,
                             x**2 + y**2 - 2*y + 2*z**2 - 5,
                             3*x**2 - 12*x + y**2 - 3*z**2 + 8])

        else:
            return np.array([x**2 - 4*x + y**2,
                             x**2 - x - 12*y + 1,
                             3*x**2 - 12*x + y**2 - 3*z**2 + 8])

def jacob(F,op):
    x = F[0]
    y = F[1]

    if op == 1:
        return np.array([[2*x + y, x],
                        [3*y**2, 6*x*y + 1]])
    
    elif op==2:
        return np.array([[2*x, 2*y],
                         [-math.e**2, -2]])

    elif op==3 or op==4:
        z = F[2]

        if op==3:
            return np.array([[4*x - 4, 2*y, 6*z + 6],
                             [2*x, 2*y - 2, 4*z],
                             [6*x - 12, 2*y, -6*z]])

        else:
            return np.array([[2*x - 4, 2*y, 0],
                             [2*x - 1, -12, 0],
                             [6*x - 12, 2*y, -6*z]])