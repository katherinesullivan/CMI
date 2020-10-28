from collections import OrderedDict

def elimina_duplicados(arr):
  return list(OrderedDict.fromkeys(arr))

def cant_elem_distintos(arr):
  return len(elimina_duplicados(arr))

print(cant_elem_distintos([1,1,1,1,1,1,1,2,3,4,2,2,5]))