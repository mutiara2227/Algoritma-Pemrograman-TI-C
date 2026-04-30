struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}


def total_ukuran(folder: dict)->int:
    total = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            total += total_ukuran(value)
        else:
            total += value
    return total

def hitung_file(folder: dict)->int:
    total = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            total += hitung_file(value)
        else:
            total += 1
    return total

def cari_terbesar(folder: dict, nama_folder="")->tuple:
    nama_file = ""
    ukuran_kb = -1
    for key, value in folder.items():
        if isinstance(value, dict):
            nama, ukuran = cari_terbesar(value, key)
        else:
            nama = key
            ukuran = value

        if ukuran > ukuran_kb:
            ukuran_kb = ukuran
            nama_file = nama

    return nama_file, ukuran_kb

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    spasi = "    " * level
    print(f"{spasi} {nama}")
    for key, value in folder.items():
        if isinstance(value, dict):
            tampilkan_tree(value, key, level + 1)
        else:
            print(f"{spasi}     {key} ({value} KB)")

a = struktur['Skripsi_Aqil']
print(f'Total Ukuran Skripsi: {total_ukuran(a)} KB')
print(f'Jumlah File: {hitung_file(a)} file')

nama,ukuran = cari_terbesar(a)
print(f'File terbesar: {nama} ({ukuran} KB)')
print('\nStruktur Folder:')
tampilkan_tree(a,'Skripsi_Aqil')

