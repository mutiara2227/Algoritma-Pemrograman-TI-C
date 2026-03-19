#Function dan Validasi Data

def rata_rata(nilai): #Buat sebuah fungsi bernama rata_rata(nilai) & Menerima sebuah list berisi nilai mahasiswa
    if nilai == []:             #Jika list kosong
        print('Data kosong')    #kembalikan pesan: "Data kosong"
        return
    jumlah = 0
    for nilai_mahasiswa in nilai:
        print(nilai_mahasiswa)
        jumlah += nilai_mahasiswa
        rata = jumlah / len(nilai)  #Menghitung rata-rata nilai
    print('Jumlah =',jumlah)
    print('Rata-rata =',rata)

#Panggil fungsi dengan list: [80, 75, 90, 60, 85]
nilai = [80, 75, 90, 60, 85]
rata_rata(nilai)

####
film = [['Danur', 50000], ['Inside Out 2', 45000], ['Avatar', 50000], ['Pengabdi Setan', 40000], ['Jumbo', 35000]]

print('DAFTAR FILM CINEMAJU')
for i in range(len(film)):
    print(i+1,'.',film[i][0], ':', film[i][1])

pilih = int(input('Masukkan nomor film : '))

if pilih >= 1 and pilih <= len(film):
    judul = film[pilih-1][0]
    harga = film[pilih-1][1]
    print('Film yang dipilih : ',judul)
    print('Harga tiket : ',harga)
else:
    print('Error: Nomor tidak valid!')