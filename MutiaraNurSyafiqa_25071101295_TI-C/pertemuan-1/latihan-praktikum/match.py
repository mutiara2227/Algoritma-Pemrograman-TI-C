#1 (Phyton Match Statement)
bulan = 'Februari'
match bulan:
    case 'Januari':
        print('awal tahun')
    case 'Februari':
        print('bulan kelahiran')

#2 (Default Value)
match bulan:
    case 'Desember':
        print('libur semester')
    case 'Januari':
        print('awal tahun')
    case _: #sebagai nilai kasus terakhir jika Anda ingin blok kode dieksekusi ketika tidak ada kecocokan lain
        print('masuk kuliah')

#3 (Combine Values)
match bulan:
    case 'Desember' | 'Januari':
        print('Waktu libur kuliah')
    case _:
        print('Bukan waktu libur kuliah')

#4 (If Statements as Guards)
nilai = 75
match nilai:
    case n if n >= 90:
        print('A')
    case n if n >= 80:
        print('B')
    case n if n >= 70:
        print('C')
    case _:
        print('Tidak lulus')
