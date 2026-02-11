#Phyton Variables

#1
x = "Umur saya"
y = 19
z = 'tahun'
print(x)
print(y)
print(z)

#2
a = 3
a = 'kelas'
print(a)

#3
a = 'good'
b = 'night'
b = 'afternoon'
c = 'everyone'
print(a)
print(b)
print(c)

#4
p = 'selamat'
q = 'malam'
r = 'semuanya'
r = 'all'
print(p,q,r)

#5
X = 'ada'
x = 3
Y = 'prodi'
y = 'dalam'
z = 'satu'
Z = 'jurusan'
z = 1
print(X,x,Y,y,z,Z)


#Variable Names
"""
Tidak boleh diawali dengan angka
Tidak boleh menggunakan spasi
Tidak boleh menggunakan tanda(-)
"""

#1
nama = 'Mutiara Nur Syafiqa' #huruf kecil semua
NIM = 25071101295 #huruf besar semua
ProgramStudi = 'S1 Teknik Informatika.' #setiap kata diawali huruf kapital tanpa spasi
print('Nama saya',nama,'dengan NIM',NIM,'prodi',ProgramStudi)

#2
_hari = 22 #boleh diawali dengan tanda(_)
bulan2 = 'Februari' #angka tidak diletakkan diawal kata
tahun = 2007
waktuLahir = '12 siang' #setiap kata, kecuali kata pertama, diawali dengan huruf kapital
tempat_lahir = 'Kota Pekanbaru.' #setiap kata dipisahkan oleh tanda(_)
print('Dia lahir pada tanggal',_hari,bulan2,tahun,'pada pukul',waktuLahir,'di',tempat_lahir)


#Assign Multiple Values

#1 (Banyak nilai untuk beberapa variabel)
namaDepan, _nama_tengah, NAMABELAKANG = 'Mutiara', 'Nur', 'Syafiqa'
print('My name is',namaDepan, _nama_tengah, NAMABELAKANG)

#2 (1 nilai untuk beberapa variabel)
a = b = c = 'Selamat datang'
print(a)
print(b) 
print(c)

#3 (ekstrak nilai dalam array ke variabel)
jurusan = ['Elektro','Teknik Mesin','Teknik Kimia']
x, y, z = jurusan
print('Teknik',x)
print(y)
print(z)


#Output Variables

#1
x, a = 'Mutiara', 'Mutiara '
y, b = 'Nur', 'Nur '
z, c = 'Syafiqa', 'Syafiqa '
print(x,y,z)
print(a + b + c)

#2
x = 25
y = 75
print (x+y)


#Global Variables

#1
x = 'selamat'

def myfunc():
    print(x + ' pagi')
    print(x + ' siang')
    print(x + ' malam')
myfunc()

