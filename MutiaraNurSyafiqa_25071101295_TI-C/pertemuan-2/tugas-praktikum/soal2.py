#Range dan Pola Bilangan
PRIMA = []
def bilangan_prima(n): #Buat sebuah fungsi bernama bilangan_prima(n)
    for x in range(2,n-1):   #Menggunakan range()
        prima = True
        for i in range(2,x):
            if x % i == 0:
                prima = False
        if prima:
            PRIMA.append(x)
    return (PRIMA) #Mengembalikan list bilangan prima dari 1 sampai n

bilangan_prima(50) #Panggil fungsi untuk n = 50
print('Bilangan prima dari 1 - 50 =',PRIMA) #Tampilkan hasilnya