#Realiza una función separar(lista) que tome una 
#lista de números enteros desordenados y devuelva
#dos listas ordenadas. La primera con los números 
#pares y la segunda con los números impares.

print ("Funcion separar lista")

listaNumerica = [10, 7, 4, 5, 8, 1, 2, 11]
print("Tu lista original es: "+ str(listaNumerica))
listaNumerica.sort()
listaordenada = listaNumerica

print(f"Despues de ordenar {listaordenada}")
	
pares = listaordenada
impares = listaordenada

for n in listaordenada:
		if n % 2 == 0:
			pares.append(n)
		else:
			impares.append(n)	

print(f"Pares Ordenados {pares}")
print(f"Impares Ordenados{impares}")
