class Buku:
    def __init__(self, judul, denda_per_hari):
        self.judul = judul
        self.denda_per_hari = denda_per_hari
    
    def tampilkan(self):
        print(f'{self.judul} - Rp{self.denda_per_hari}/hari')
    
    def denda(self):
        return self.denda_per_hari
    
class Peminjaman:
    def __init__ (self):
        self.judul = None
        self.total_denda = 0
    
    def tambah (self, judul, hari_terlambat):
        self.judul = judul
        self.hari_terlambat = hari_terlambat
        self.total_denda += hari_terlambat * self.judul.denda_per_hari
    
    def ringkasan(self):
        print(f'total denda anda adalah : {self.total_denda}')
    
    
buku1 = Buku('C', 2000)
buku2 = Buku('python', 2500)
buku3 = Buku('cpp', 1500)


buku_buku = [buku1, buku2, buku3]

for i in range(len(buku_buku)):
    print(f'{i+1}.', end=" ")
    buku_buku[i].tampilkan()
  
buku_yg_mana = int(input('mau buku yg mana? 1/2/3 : '))
terlambat = int(input('masukkan berapa lama anda terlambat mengembalikan : '))

pinjam = Peminjaman()

pinjam.tambah(buku_buku[buku_yg_mana], terlambat)

pinjam.ringkasan()

