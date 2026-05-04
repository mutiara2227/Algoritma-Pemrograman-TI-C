#####PERBAIKAN#####

# =========================
# VARIABEL DASAR
# =========================
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]


# =========================
# BAGIAN A - FUNGSI INTI
# =========================

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    """Menentukan pemenang antara pemain dan komputer."""
    
    if pilihan_pemain == pilihan_komputer:
        return "seri"
    
    if (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
       (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
       (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        return "pemain"
    
    return "komputer"


def main_satu_giliran(nomor_giliran):
    """Menjalankan satu giliran permainan."""
    
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    
    # Validasi input pemain
    while True:
        pilihan_pemain = input("Pilih (gunting/batu/kertas): ").lower()
        if pilihan_pemain in ["gunting", "batu", "kertas"]:
            break
        print("Input tidak valid, ulangi!")

    print("Komputer memilih:", pilihan_komputer)

    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    print("Hasil giliran:", hasil)

    return hasil


def main_satu_ronde(nama, nomor_ronde):
    """Menjalankan satu ronde permainan hingga salah satu mencapai 3 kemenangan."""
    
    menang_pemain = 0
    menang_komputer = 0
    giliran = 0

    while menang_pemain < 3 and menang_komputer < 3:
        print(f"\n--- Giliran {giliran + 1} ---")
        hasil = main_satu_giliran(giliran)

        if hasil == "pemain":
            menang_pemain += 1
        elif hasil == "komputer":
            menang_komputer += 1

        giliran += 1

        print(f"Skor sementara -> {nama}: {menang_pemain} | Komputer: {menang_komputer}")

    # Menentukan pemenang ronde
    if menang_pemain > menang_komputer:
        print("\nPemenang ronde:", nama)
        skor = giliran * 10
    else:
        print("\nPemenang ronde: Komputer")
        skor = 0

    return [nama, skor]


# =========================
# BAGIAN B - RIWAYAT
# =========================

def tampilkan_riwayat(riwayat):
    """Menampilkan semua riwayat permainan dalam bentuk tabel."""
    
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
        return

    print("\n===== RIWAYAT PERMAINAN =====")
    print("No | Nama | Skor")
    print("--------------------")

    for i in range(len(riwayat)):
        print(f"{i+1}  | {riwayat[i][0]} | {riwayat[i][1]}")


# =========================
# BAGIAN C - BUBBLE SORT
# =========================

def bubble_sort_riwayat(riwayat):
    """Mengurutkan riwayat berdasarkan skor tertinggi (tanpa mengubah data asli)."""
    
    data = riwayat[:]  # salinan list

    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def tampilkan_leaderboard(riwayat):
    """Menampilkan leaderboard berdasarkan skor tertinggi."""
    
    if len(riwayat) == 0:
        print("Belum ada data leaderboard.")
        return

    data_urut = bubble_sort_riwayat(riwayat)

    print("\n===== LEADERBOARD =====")

    for i in range(len(data_urut)):
        tanda = " *" if i == 0 else ""
        print(f"{i+1}. {data_urut[i][0]} - {data_urut[i][1]}{tanda}")


# =========================
# PROGRAM UTAMA
# =========================

riwayat = []

nama = input("Masukkan nama pemain: ")
nomor_ronde = 1

while True:
    print(f"\n=== RONDE {nomor_ronde} ===")
    
    hasil = main_satu_ronde(nama, nomor_ronde)
    riwayat.append(hasil)

    lanjut = input("\nMain lagi? (ya/tidak): ").lower()
    if lanjut != "ya":
        break

    nomor_ronde += 1


# OUTPUT AKHIR
tampilkan_riwayat(riwayat)
tampilkan_leaderboard(riwayat)

print("\nSesi permainan selesai!")




####ASLI#####
#==================
#=====BAGIAN A=====
#==================

DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

riwayat =[]
def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    menang_lawan = {'gunting':'kertas', 'batu':'gunting', 'kertas':'batu'}
    
    if pilihan_pemain == pilihan_komputer:
        return 'seri'
    elif menang_lawan[pilihan_pemain] == pilihan_komputer:
        return 'pemain'
    else:
        return 'komputer'

def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    while True:
        tebakan = input ('Batu/Gunting/Kertas? >>').lower()
        if tebakan in DAFTAR_PILIHAN :
            print(tebakan)
            break
        print('pilihan tidak valid')
    hasil = tentukan_pemenang(tebakan, pilihan_komputer)
    if hasil == 'pemain' or hasil =='komputer':
        print('=====================')
        print(hasil+' menang')
        print('=====================')
        print('komputer : ', pilihan_komputer)
        print('pemain : ',pilihan_pemain)

def main_satu_ronde(nama,nomor_ronde):
    nomor_giliran = 0
    menang_pemain = 0
    menang_komputer = 0
    while menang_pemain < 3 and menang_komputer < 3:
        hasil = main_satu_giliran(nomor_giliran)
        nomor_giliran += 1
        if hasil == 'pemain':
            menang_pemain += 1
        elif hasil == 'komputer':
            menang_komputer += 1




tentukan_pemenang('gunting','kertas')
main_satu_giliran(3)
main_satu_ronde()

