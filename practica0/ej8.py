from math import log

def es_potencia_de_dos (a):
    #ver que no tenga coma
    if (log(a, 2) - int(log(a,2)) == 0):
      return 1
    else:
      return 0

def suma_orden (a,b):
    suma = 0
    for i in range (a, b+1):
      if (es_potencia_de_dos(i)):
        suma = suma + i
    return suma

def suma_potencias_dos (a,b):
    if (a <= b):
        suma = suma_orden(a, b)
        print(suma)
    else:
        suma = suma_orden(b, a)
        print(suma)
    return 0

suma_potencias_dos(2,8)

print(es_potencia_de_dos(2))