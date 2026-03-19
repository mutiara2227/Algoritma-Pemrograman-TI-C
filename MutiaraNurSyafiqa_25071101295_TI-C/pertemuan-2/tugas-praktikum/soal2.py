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



####
film = [['Danur', 50000], ['Inside Out 2', 45000], ['Avatar', 50000], ['Pengabdi Setan', 40000], ['Jumbo', 35000]]

pembelian = []

print('DAFTAR FILM CINEMAJU')
for i in range(len(film)):
    print(i+1,'.',film[i][0], ':', film[i][1])

while True:
    pilih = int(input('Masukkan nomor film (0 untuk selesai pilih): '))

    if pilih == 0:
        break

    if pilih >= 1 and pilih <= len(film):
        judul = film[pilih-1][0]
        harga = film[pilih-1][1]

        jumlah = int(input('Masukkan jumlah tiket: '))
        pembelian.append([judul, harga, jumlah])

        print('Film yang dipilih :', judul)
        print('Harga tiket :', harga)
    else:
        print('Error: Nomor tidak valid!')

print('\nDAFTAR PEMBELIAN TIKET')
total = 0
for x in pembelian:
    judul = x[0]
    harga = x[1]
    jumlah = x[2]
    total_sementara = harga*jumlah

    print(judul, '(', jumlah,'tiket ) =', total_sementara)
    total += total_sementara

print('Total harga :',total)
