def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)

from collections import OrderedDict

def elimina_duplicados(arr):
  return list(OrderedDict.fromkeys(arr))
  
print(elimina_duplicados([1,2,3,3,3,3,4,5,1,5]))



#https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
