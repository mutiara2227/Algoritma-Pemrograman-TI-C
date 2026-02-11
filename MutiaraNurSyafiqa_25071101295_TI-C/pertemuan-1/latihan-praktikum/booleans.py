#1 (Boolean Values)
a = 200
b = 33
if b > a:
  print("b lebih besar dari a")
else:
  print("b lebih kecil dari a")

#2 (Evaluate Values and Variables)
print(bool("umur")) #evaluasi sebuah string dan sebuah angka
print(bool(19))
x = 'umur'          #evaluasi 2 variabel
y = 19
print(bool(x))
print(bool(y))

#3 (Some Values are False)
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#4 (Functions can Return a Boolean)
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")