###PERBAIKAN###
data = [["Algoritma", 2000], ["Basis Data", 2500], ["C", 3000], ["List", 3500], ["Dicti", 1000]]


while True:
    pilihan = int(input('masukkan nomor buku 1/2/3/4/5 (0 untuk keluar) : '))
    if pilihan == 0:
        break
    terlambat = int(input('berapa lama anda terlambat?: '))
  
    print(f'Buku yang dipinjam : {data[pilihan-1][0]}')
    print(f'Terlambat : {terlambat} hari')
    print(f'Denda : {terlambat*data[pilihan-1][1]}')


###ASLI###
buku = [['Algoritma',2000],['Basis Data',2500],['Struktur Data',3000],['Aljabar',4000],['Statistika',1000]]

peminjaman =[]

print('DAFTAR BUKU CERDAS ILMU')

for i in range(len(buku)):
    print(i+1,'.',buku[i][0], ':', buku[i][1])


while True:
    pilih = int(input('Masukkan nomor buku yg mau dipinjam (0 untuk selesai pilih): '))
    keterlambatan = int(input('Masukkan jumlah hari keterlambatan : '))
    
    if pilih == 0:
        break
    
    if pilih >= 1 and pilih <= len(buku):
        judul = buku[pilih-1][0]
        denda = buku[pilih-1][1]
        
        lama_pinjam = int(input('Berapa hari pinjam : '))
        peminjaman.append([judul, denda, lama_pinjam])
    
        print('Buku yang dipilih : ',judul)
        print('Lama peminjaman : ',lama_pinjam,'hari')

    else:
        print('Error: Nomor tidak valid!')

    if keterlambatan < 0:
        print('Error: Keterlambatan tidak boleh kurang dari nol')

    
