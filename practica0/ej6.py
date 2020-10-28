# la función toma dos nros y devuelve la cantidad de nros que son múltiplos del primero
# y menores que el segundo
def dos_numeros_for(a, b):
    cant = 0
    if (a >= b):
      return 0
    for i in range(1, b+1):
      if (a*i > b):
        return cant
      else:
        cant+=1
    return cant

def dos_numeros_while(a,b):
    cant = 0
    while (a*cant < b):
      cant+=1
    return cant-1
    #resto uno pq le sume innnecesariamente


print(dos_numeros_while(1, 10))