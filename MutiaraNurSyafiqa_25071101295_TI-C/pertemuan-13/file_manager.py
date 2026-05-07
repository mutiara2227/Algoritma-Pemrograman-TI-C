import os

while True:
    print('====================================')
    print('PYTHON FILE MANAGER v1.0')
    print('====================================')
    print("[1] Read File")
    print("[2] Write File")
    print("[3] Delete File")
    print("[0] Exit")

    pilih = input("Pilih menu: ")

    # READ FILE
    if pilih == "1":
        files = [f for f in os.listdir() if f.endswith(".txt")]

        if len(files) == 0:
            print("Tidak ada file .txt ditemukan")
        else:
            print("\nFile Tersedia :")
            for i in range(len(files)):
                print(f"[{i+1}] {files[i]}")

            try:
                nomor = int(input("Pilih file (nomor): "))
                file = files[nomor - 1]

                f = open(file, "r")
                print("\nIsi File:\n")
                print(f.read())
                f.close()

            except:
                print("Input tidak valid")

    # WRITE FILE
    elif pilih == "2":
        nama_file = input("Nama file: ")

        if not nama_file.endswith(".txt"):
            nama_file += ".txt"

        isi = input("Isi file: ")

        f = open(nama_file, "w")
        f.write(isi)
        f.close()

        print("File berhasil disimpan")

    # DELETE FILE
    elif pilih == "3":
        files = [f for f in os.listdir() if f.endswith(".txt")]

        if len(files) == 0:
            print("Tidak ada file .txt ditemukan")
        else:
            print("\nDaftar File:")
            for i in range(len(files)):
                print(f"[{i+1}] {files[i]}")

            try:
                nomor = int(input("Pilih file: "))
                file = files[nomor - 1]

                yakin = input("Yakin ingin hapus? (y/n): ")

                if yakin == "y":
                    os.remove(file)
                    print("File berhasil dihapus")
                else:
                    print("Batal hapus")

            except:
                print("Input tidak valid")

    # EXIT
    elif pilih == "0":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")