def max_de_tres ():
    a = input("Ingrese 3 números: \n")
    b = input()
    c = input()
    if (a >= b):
      if (a >= c):
        return a
      else:
        return c
    else:
      if (b >= c):
        return b
      else:
        return c

print("El máximo es", max_de_tres())      