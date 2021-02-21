"""
Escribir una función dia_siguiente_t que dada 
una fecha expresada como la terna
(Día, Mes, Año) (donde Día y Año son
números enteros, y Mes es el texto Ene, Feb, ...,
Dic, según corresponda) calcule el día siguiente 
al dado, en el mismo formato.
"""
meses_String_a_Int = {"Ene": 1,"Feb":2,"Mzo":3,"Abr":4, "May":5,"Jun":6,"Jul":7,"Ago":8,"Sep":9,"Oct":10,"Nov":11,"Dic":12,}
meses_Int_String = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
def dia_siguiente_e():
  print("CLAVE DE LOS MESES: \nEnero: Enero \nFebrero: Febrero \nMarzo:Marzo \nAbril:Abril \n\
  Mayo:Mayo \nJunio:Junio \nJulio:Julio \nAgosto:Agosto \nSeptiembre:Septiembre \nOctubre:Octubre \nNoviembre:Noviembre \nDiciembre:Diciembre")
  fecha = input(f"Escribe una fecha [Usando el formato dia,mes,año (00/III/0000)]: ")
  dia = int(fecha[slice(0,2)])
  mes = meses_String_a_Int[(fecha[slice(3,6)])]
  año = int(fecha[slice(7,11)])
  if mes > 12:
    return ("El mes ingresado no es valido")
  elif mes == 2 and dia > 29:
    return ("La fecha ingresada no es valida ")
  elif(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
    return("La fecha ingresada no es valida")
  elif (mes == 4 or mes == 6 or mes ==9 or mes == 11) and dia>30:
    return ("La fecha ingresada no es valida")
  else:
    if dia < 28:
      dia += 1
    else:
      if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes ==10 or mes == 12:
        if dia < 31:
          dia += 1
        else:
          dia = 1
          if mes < 12:
            mes += 1
          else:
            mes= 1
            año += 1
      elif mes == 4 or mes == 6 or mes ==9 or mes ==11:
        if dia<30:
          dia += 1
        else:
          dia = 1
          mes += 1
      else:
        dia = 1
        mes += 1
  return (f"{dia}/{meses_Int_String[mes]}/{año}")

print(dia_siguiente_e())


