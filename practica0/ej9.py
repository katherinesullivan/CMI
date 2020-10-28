def hay_duplicados(arr):
    seto = set(arr)
    if (len(seto) < len(arr)):
        return 1
    else:
        return 0

print(hay_duplicados([1,2,3,'a','b']))