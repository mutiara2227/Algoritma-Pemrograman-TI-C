class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
    
    def sound(self):
        print('suara')
    
class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, kepemilikan):
        super().__init__(jenis, merk, tahun_rilis)
        self.__kepemilikan = kepemilikan

    def get_kepemilikan(self):
        return self.__kepemilikan
    

        
class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, kepemilikan):
        super().__init__(jenis, merk, tahun_rilis)
        self.__kepemilikan = kepemilikan

    def get_kepemilikan(self):
        return self.__kepemilikan
    
v1 = Vehicle('Toyota','Yaris',2001)
v1.sound()

m1 = Mobil('Toyota','Avanza',2002,'Mutiara')
print(m1.get_kepemilikan())

m2 = Motor('Honda','Beat',2003,'Syafiqa')
print(m2.get_kepemilikan())

