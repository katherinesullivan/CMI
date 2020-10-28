def num_vocales(s):
  cant = 0
  vowels = ['a','e','i','o','u']
  for i in range(len(s)):
    if (s[i].lower() in vowels):
        cant+=1
  return cant

print(num_vocales("kjEEsdgfAkjdiih"))