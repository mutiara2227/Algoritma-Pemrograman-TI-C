#Aritmetic

x = 17
y = 3
print(x + y) #tambah
print(x - y) #kurang
print(x * y) #kali
print(x / y) #bagi
print(x % y) #sisa hasil bagi
print(x ** y)#pangkat
print(x // y)#pembulatan kebawah


#Assignment

x = 17      
x += 3 #x = x + 3
print(x)
x -= 3 #x = x - 3
print(x)
x *= 3 #x = x * 3	
print(x)
print(x := 3) #walrus operator (menetapkan nilai ke variabel sebagai bagian dari ekspresi yang lebih besar)


#Comparison

x = 17
y = 3
print(x == y) #sama dengan
print(x != y) #tidak sama dengan
print(x > y) #lebih besar
print(x < y) #lebih kecil
print(x >= y) #besar sama
print(x <= y) #kecil sama


#Logical

x = 6
print(x < 5 and  x < 10) #True jika kedua statement true
print(x < 5 or x < 4) #True jika salah satu statement true
print(not(x < 5 and x < 10)) #Jika true maka output False dan sebaliknya


#Identity
"""is - Memeriksa apakah kedua variabel menunjuk ke objek yang sama di memori.
   == - Memeriksa apakah nilai kedua variabel sama"""

x = [1,2,3]
y = [1,2,3]
z = x
print(x is z) #True jika objek 2 variabel sama
print(x is not y) #True jika objek 2 variabel tidak sama


#Bitwise

print(10 & 5) 
print(10 | 5)
print(10 ^ 5)


#Operator Precedence
print((10 + 5) - (1 + 3)) #ekspresi di dalam tanda kurung harus dievaluasi terlebih dahulu
print(100 + 5 * 3) #perkalian dievaluasi sebelum penjumlahan
print(5 + 4 - 7 + 3) #jika prioritas sama, evaluasi dari kiri


