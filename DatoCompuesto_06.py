"""
Escribir una función dia_siguiente_e 
que dada una fecha expresada como la terna
(Día, Mes, Año) (donde Día, Mes y Año 
son números enteros) calcule el día siguiente
al dado, en el mismo formato.
"""
def fecha_dia_siguiente(dia,mes,año):
    bisiesto = False

    if año % 400 == 0 :
        bisiesto = True
    elif año % 4 == 0:
        bisiesto = True

    if mes in(1,3,5,7,8,10,12):
        diasMes = 31
    elif mes ==2:
        if bisiesto:
            diasMes = 29
        else:
            diasMes=28
    else:
        diasMes = 30
    
    if dia < diasMes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            año += 1
        else:
            mes=1
    return(dia,mes,año)


print(fecha_dia_siguiente(20,2,2021))
print(fecha_dia_siguiente(21,2,2021))
print(fecha_dia_siguiente(31,12,2020))
print(fecha_dia_siguiente(3,12,2021))
print(fecha_dia_siguiente(1,2,2020))