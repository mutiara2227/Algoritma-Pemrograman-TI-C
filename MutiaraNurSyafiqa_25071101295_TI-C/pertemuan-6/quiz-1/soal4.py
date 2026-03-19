minggu = int(input('masukkan jumlah minggu : '))
kategori_buku = int(input('masukkan jumlah kategori : '))

data = []

for i in range(minggu):
    baris = []
    for j in range(kategori_buku):
        jumlah_buku = int(input(f'masukkan jumlah buku pada minggu ke-{i+1} kategori ke-{j+1} : '))
        baris.append(jumlah_buku)
    data.append(baris)


for i in range(minggu):
    print(f'minggu ke-{i+1} = {sum(data[i])}')
  
for i in range(kategori_buku):
    total = 0
    for j in range(minggu):
        total += data[j][i]
    print(f'kategori {i+1} = {total}')