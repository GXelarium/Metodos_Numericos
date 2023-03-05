import Newton
import numpy as np

def menu():
    print(""" PROGRAMA 1: MÉTODO DE NEWTON RAPHSON
        
        Elíge un sistema de ecuaciones:

        1)   
                f1(x,y) = x² + xy - 10 = 0
                f2(x,y) = y + 3xy² - 50 = 0
        
        2)
                f1(x,y) = x² + y² - 9 = 0
                f2(x,y) =-e^x - 2y - 3 = 0
        
        3)
                f1(x,y,z) = 2x² - 4x + y² + 3z² + 6z + 2 = 0
                f2(x,y,z) = x² + y² - 2y + 2z² - 5 = 0
                f3(x,y,z) = 3x² - 12x + y² - 3z² + 8 = 0

        4) 
                f1(x,y,z) = x² - 4x + y**2 = 0
                f2(x,y,z) = x² - x - 12y + 1 = 0
                f3(x,y,z) = 3x² - 12x + y² - 3z² + 8 = 0

       """)

    opcion = int(input("Sistema número: "))
    if opcion > 0 and opcion < 5:
        X = list(map(float, input("Introduce el punto inicial separado por comas: ").split(',')))
        max = int(input("Introduce el máximo de iteraciones: "))
        tol = float(input("Introduce la tolerancia: "))
        metodo = Newton.metodo(X,max,tol,opcion)
        print(metodo)
    else:
        print("Escoge un sistema válido")

    
    





if __name__ == '__main__':

    menu()
    # X = np.array([1.5,1.5])
    # opcion = 1
    # prueba = Newton.metodo(X,op=opcion)
    # print(prueba)
