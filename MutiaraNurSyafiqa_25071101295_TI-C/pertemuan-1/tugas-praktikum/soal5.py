#Buat sebuah fungsi bernama hitung(a, b) yang menerima dua parameter a dan b
def hitung(a, b):
#Mengembalikan hasil penjumlahan a + b
    tambah = a + b
#Mengembalikan hasil pengurangan a - b
    kurang = a - b
    return(tambah,kurang)
#Panggil fungsi tersebut
PENJUMLAHAN,PENGURANGAN = hitung(15, 8)
#Tampilkan hasil penjumlahan dan pengurangannya ke layar
print('Penjumlahan =',PENJUMLAHAN)
print('Pengurangan =',PENGURANGAN)