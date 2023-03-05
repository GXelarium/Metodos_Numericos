import Newton
import numpy as np
import os

def limpiar():
        if os.name == "posix":
                os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system ("cls")

def metodo(opcion):
        X = list(map(float, input("Introduce el punto inicial separado por comas: ").split(',')))
        max = int(input("Introduce el máximo de iteraciones: "))
        tol = float(input("Introduce la tolerancia: "))
        metodo = Newton.metodo(X,max,tol,opcion)
        print(metodo)


def menu():
    print(""" PROGRAMA 1: MÉTODO DE NEWTON RAPHSON

Elaborado por:
-López Medina Andrés Alejandro


        
        Elige un sistema de ecuaciones:

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

    opcion = int(input("Sistema de ecuaciones número: "))
    if opcion > 0 and opcion < 5:
        loop = True
        while loop:
                metodo(opcion)
                estado = input("¿Quieres introducir otros valores? S/N: ").lower()
                if estado != 's':
                     loop = False
    else:
        print("Escoge un sistema válido")

    
    





if __name__ == '__main__':
    loop = True
    while loop:
        limpiar()
        menu()
        estado = input("¿Quieres resolver otro sistema? S/N: ").lower()
        if estado != 's':
             loop = False
        

    # X = np.array([1.5,1.5])
    # opcion = 1
    # prueba = Newton.metodo(X,op=opcion)
    # print(prueba)
