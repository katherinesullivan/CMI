def longitud_string():
    a = input("Ingrese cadena: ")
    return len(a)

def longitud_array_char():
    a = input("Ingrese cadena para formar array con chars: ")
    list1 = []
    list1[:0] = a
    #list1 = list(a)
    return len(list1)

def longitud_array_words():
    a = input("Ingrese cadena para formar array con palabras: ")
    list1 = list(a.split(" "))
    return len(list1)

def longitud():
    a = int(input("Ingrese \n1 si quiere la longitud de su string \n2 si quiere la cantidad de palabras en su string \n"))
    if (a == 1):
      return longitud_array_char()
    elif (a == 2):
      return longitud_array_words()
    else:
      print("Comando inválido \n")
      return 0

print("La longitud es", longitud())