def es_primo(a):
  if (a < 2):
    return 0
  else:
    x = 2
    while (x*x <= a):
      if (a%x == 0):
        return 0
      x+=1
  return 1

def nros_primos_hasta (n):
    for i in range(1, n):
      if (es_primo(i) == 1):
        print(i)
    return 0

nros_primos_hasta(10000)

print(es_primo(169))

# https://www.geeksforgeeks.org/analysis-different-methods-find-prime-number-python/
