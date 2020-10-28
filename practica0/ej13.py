def palabras_de_mas_de_5 (s):
    a = s.split(" ")
    cant = 0
    for i in range(len(a)):
      if (len(a[i]) > 5):
          cant+=1
    return cant

print(palabras_de_mas_de_5("jajajjaja avchu bebesss"))