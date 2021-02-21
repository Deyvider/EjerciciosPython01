"""
Escribir un programa que pregunte al 
usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los 
muestre por pantalla ordenados de menor a
mayor. Escribir un programa que almacene en
una lista los números del 1 al 10 y los
muestre por pantalla en orden inverso separados por comas.
"""

print("PROGRAMA 1")
loteria = []

while True:
    print("1.-Ingresar Numeros de la loteria \n 0.- Salir")
    op = int(input("Ingresa una opcion->"))
    if(op == 1):
        n = input("Ingrese el numero:")
        loteria.append(n) 
    if(op == 0):
        break

print("Los ganadores son: "+ str(loteria))
loteria.sort()
print("Los numeros ganadores ordenados son: " + str(loteria))

print("Programa 2")

num=[1,2,3,4,5,6,7,8,9,10]
num.reverse()
print("Los numeros invertidos son: "+str(num))
