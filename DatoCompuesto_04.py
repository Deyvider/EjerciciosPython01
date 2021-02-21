"""
Proponer una representación con tuplas para 
las cartas de la baraja francesa. Escribir 
una función poker que recibe cinco cartas 
de la baraja francesa e informe
(devuelva el valor lógico correspondiente)
si esas cartas forman o no un poker (es
decir que hay 4 cartas con el mismo número).
"""
import random
corazon = ("cA","c2","c3","c4","c5","c6","c7","c8","c9","cJ","cQ","cK")
picas =("pA","p2","p3","p4","p5","p6","p7","p8","p9","pJ","pQ","pK")
trebol = ("tA","t2","t3","t4","t5","t6","t7","t8","t9","tJ","tQ","tK")
rombos = ("rA","r2","r3","r4","r5","r6","r7","r8","r9","rJ","rQ","rK")
baraja = corazon + picas + trebol + rombos

barajar = list(baraja)
random.shuffle(barajar)

def poker (cartas):
    mazo = random.sample(cartas,5)
    print(f"Mazo actual: \n{mazo}")
    for i in range(2):
        rev = mazo [i]
        cont = 0
        for j in range(0,5):
            cartas = mazo[1]
            if rev[1] == cartas[1]:
                cont += 1
        if cont > 3:
            print("Felicidades \n tienes \n un poker\n")
            break
    else:
        print("No tienes Poker")

poker(barajar)
