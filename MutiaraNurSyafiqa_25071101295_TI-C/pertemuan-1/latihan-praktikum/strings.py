#Python Strings

#1 (tanda kutip dalam string harus beda dengan tanda kutip string)
print('ibu bertanya "kamu sudah makan?"')
print("hari jum'at")

#2 (Multiline Strings)
biodata = """Nama : Mutiara Nur Syafiqa
NIM : 25071101295
Prodi : S1 Teknik Informatika"""
print(biodata)  

biodata = '''Nama : Mutiara Nur Syafiqa
NIM : 25071101295
Prodi : S1 Teknik Informatika'''
print(biodata)  

#3 (Strings are Arrays)
nama = "Mutiara, Nur, Syafiqa"
print(nama[0])
print(nama[1])
print(nama[2])

#4 (String Length)
nama = 'MUTIARA NUR SYAFIQA'
print(len(nama))

#5 (Check String)
nama = 'mutiara nur syafiqa'
print('nur' in nama)
if 'nur' in nama:
    print('ya, "nur" ada didalam nama')

#6 (Check if not)
nama = 'mutiara nur syafiqa'
print('assyifa'not in nama)
if 'assyifa' not in nama:
    print('tidak,"assyifa" tidak ada didalam nama')


#Slicing Strings

a = 'mutiara nur syafiqa'
print(a[5:10]) #slicing
print(a[:8]) #slice form the start
print(a[1:]) #slice to the end
print(a[-10:-5]) #negative indexing 


#Modify Strings

a = "mutiara nur syafiqa"
print(a.upper()) #upper case
print(a.lower()) #lower case
print(a.strip()) #remove whitespace
print(a.replace("m", "t")) #replace string
print(a.split(",")) #split string


#String Concatenation

a = 'Selamat'
b = 'Pagi'
c = a + b #gabungkan variabel a dan b dalam c, tanpa spasi
print(c)
c = a + " " + b #abungkan variabel a dan b dalam c, ada spasi
print(c)


#Format String

umur = 16
KeteranganUsia = f'Saya berumur {umur} tahun' #F-Srings
print(KeteranganUsia)  
harga = 50
keteranganHarga = f'Harga baju itu adalah {harga:.3f} rupiah' #dengan menambahkan desimal
print(keteranganHarga)
_keteranganHarga = f'Harga baju itu adalah {100/2:.3f} rupiah' #dengan operasi matematika
print(_keteranganHarga)


#Escape Characters

a = 'selamat\'pagi' #single qoute
b = 'selamat\npagi' #new line
c = 'selamat\rpagi' #carriage return
d = 'selamat\tpagi' #tab
e = 'selamat\bpagi' #backspace
print(a)
print(b)
print(c)
print(d)
print(e)


