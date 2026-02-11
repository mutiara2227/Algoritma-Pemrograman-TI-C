#1 (mengulang suatu urutan (baik berupa list, tuple, dictionary, set, atau string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print('\n')

#2 (Looping String)
for x in "banana":
  print(x)

#3 (Break Statement)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == 'banana':
    break #banana diprint

for x in fruits:
  if x == 'banana':
    break #banana tidak diprint
  print(x) 

#4 (Continue Statement)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue # menghentikan iteration loop saat ini, dan melanjutkan berikutnya
  print(x) 

#5 (The Range() Function)
for x in range (2, 5):
  print (x)

#6 (Else Statement)
for x in range(1, 8):
   if (x % 2 == 0):
    print(f'{x} adalah genap')
   else:
    print(f'{x} adalah ganjil')

