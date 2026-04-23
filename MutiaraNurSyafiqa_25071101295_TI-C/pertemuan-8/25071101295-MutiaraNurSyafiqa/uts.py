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

