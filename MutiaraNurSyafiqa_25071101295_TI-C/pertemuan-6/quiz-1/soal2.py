###PERBAIKAN###
data = [["Algoritma", 2000], ["Basis Data", 2500], ["C", 3000], ["List", 3500], ["Dicti", 1000]]

for buku in range(len(data)):
    print(f'{buku+1}. Nama Buku : {data[buku][0]}')
    print(f'   Denda Keterlambatan Buku : {data[buku][1]}')


judul_buku = []

while True:
    pilihan = int(input('masukkan nomor buku 1/2/3/4/5 (0 untuk keluar) : '))
    if pilihan == 0:
        break
  
    lama_pinjam = int(input('berapa hari ingin meminjam? : '))
    judul_buku.append([data[pilihan][0], lama_pinjam, data[pilihan][1]])
  

print('daftar buku yang anda pinjam dan denda terlambat sehari')
for i in range(len(judul_buku)):
    print(f'{i+1}. {judul_buku[i][0]}, Denda : {judul_buku[i][2]} ')


###ASLI###
buku = [['Algoritma',2000],['Basis Data',2500],['Struktur Data',3000],['Aljabar',4000],['Statistika',1000]]

peminjaman =[]

print('DAFTAR BUKU CERDAS ILMU')

for i in range(len(buku)):
    print(i+1,'.',buku[i][0], ':', buku[i][1])

while True:
    pilih = int(input('Masukkan nomor buku yg mau dipinjam (0 untuk selesai pilih): '))

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

print('\nDAFTAR PEMINJAMAN BUKU')
total_denda = 0
for x in peminjaman:
    judul = x[0]
    denda = x[1]
    lama_pinjam = x[2]
    denda_sementara = denda*lama_pinjam

    print(judul, '(', lama_pinjam,'hari ) =', denda_sementara)
    total_denda += denda_sementara

print('Total Denda (Lambat 1 hari) : ',total_denda)


