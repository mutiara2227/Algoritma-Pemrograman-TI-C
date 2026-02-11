#1 (int, float, complex)
x = -8      #(Int) Bilangan bulat positif/negatif, tanpa desimal
y = -0.8    #(Float) Bilangan positif/negatif yang memiliki satu/lebih angka desimal
z = 4+5j    #(Complex) Bilangan kompleks ditulis dengan huruf "j" sebagai bagian imajiner
print(x,y,z)
print(type(x),type(y),type(z))

#2 (konversi dari satu tipe ke tipe lain)
x = 5
y = 12e3
z = -3j         #complex tidak bisa di konversi
#int to float
a = float(x)
#float to int
b = int(y)
#int to complex
c = complex(x)
print(a,b,c)
print(type(a),type(b),type(c))

#3 (angka random)
import random
print(random.randrange(1, 100))