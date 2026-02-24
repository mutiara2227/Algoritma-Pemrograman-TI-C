class Kecepatan:
    def __init__(self):
        self.jarak = 0
        self.waktu = 0
    
    def input_data(self):
        while True:
            try:
                self.jarak = float(input('Masukkan jarak(km): '))
                self.waktu = float(input('Masukkan waktu(jam): '))
                if self.jarak < 0:
                    raise ValueError('Jarak tidak boleh negatif')
                if self.waktu <= 0:
                    raise ValueError('Waktu tidak boleh nol dan negatif')
            except ValueError as e:
                print('Terjadi Kesalahan:',e)
            else:
                return True
    
    def hitung(self):
        return self.jarak / self.waktu
    
    def tampilkan_hasil(self):
        kecepatan = self.hitung()
        print('Kecepatan = ',kecepatan,'km/jam')

kec1 = Kecepatan()
kec1.input_data()
kec1.tampilkan_hasil()
print('PROGRAM SELESAI')
