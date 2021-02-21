"""
El tiempo como tuplas.
1. Proponer una representación con tuplas para representar el tiempo.
2. Escribir una función sumaTiempo que reciba dos tiempos dados y devuelva
su suma.
"""

Tiempo = (20,2,2021)

print(f"Día: {Tiempo[0]}")
print(f"Mes: {Tiempo[1]}")
print(f"Año: {Tiempo[2]}")

def sumaTiempo(t1,t2):
    s = t1+t2
    print("La suma de tiempo es: "+ str(s))
    


print("Ingrese el primer tiempo")
t1 = int(input("-> "))

print ("Ingrese el segundo tiempo")
t2 = int(input("-> "))

sumaTiempo(t1,t2)

