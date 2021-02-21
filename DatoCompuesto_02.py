# Escribir un programa que almacene las 
# asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia
# y Lengua) en una lista y la muestre por
# pantalla.

#VERSION PRO

materias = []

while True:
    print("1.- Ir a la seccion de materias \n 0.- Salir")
    op = int(input("Ingresa una opcion->"))
    if(op == 1):
        ma = input("Ingrese la materia:")
        materias.append(ma) 
    if(op == 0):
        break
print("Las materias registradas son: " + str(materias))

""" VERSION SENCILLA

mt = ['español','matematicas','quimica','historia']
print(f"Tus Materias son {mt}")"""
