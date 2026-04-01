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

