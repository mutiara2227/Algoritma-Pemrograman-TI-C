###PERBAIKAN###
data = [["Algoritma", 2000], ["Basis Data", 2500], ["C", 3000], ["List", 3500], ["Dicti", 1000]]

for buku in range(len(data)):
    print(f'{buku+1}. Nama Buku : {data[buku][0]}')
    print(f'   Denda Keterlambatan Buku : {data[buku][1]}')
  
pilihan = int(input('masukkan nomor buku 1/2/3/4/5 : '))

if pilihan == 1:
    print(f'Nama Buku : {data[0][0]}')
    print(f'Denda Keterlambatan Buku : {data[0][1]}')

elif pilihan == 2:
    print(f'Nama Buku : {data[1][0]}')
    print(f'Denda Keterlambatan Buku : {data[1][1]}')
  
elif pilihan == 3:
    print(f'Nama Buku : {data[2][0]}')
    print(f'Denda Keterlambatan Buku : {data[2][1]}')
  
elif pilihan == 4:
    print(f'Nama Buku : {data[3][0]}')
    print(f'Denda Keterlambatan Buku : {data[3][1]}')
  
elif pilihan == 5:
    print(f'Nama Buku : {data[4][0]}')
    print(f'Denda Keterlambatan Buku : {data[4][1]}')
  
else:
    print('nomor tidak valid')


###ASLI###
buku = [['Algoritma',2000],['Basis Data',2500],['Struktur Data',3000],['Aljabar',4000],['Statistika',1000]]

print('DAFTAR BUKU CERDAS ILMU')

for i in range(len(buku)):
    print(i+1,'.',buku[i][0], ':', buku[i][1])

pilih = int(input('Masukkan nomor buku : '))

if pilih >= 1 and pilih <= len(buku):
    judul = buku[pilih-1][0]
    denda = buku[pilih-1][1]
    print('Buku yang dipilih : ',judul)
    print('Denda per hari : ',denda)
else:
    print('Error: Nomor tidak valid!')