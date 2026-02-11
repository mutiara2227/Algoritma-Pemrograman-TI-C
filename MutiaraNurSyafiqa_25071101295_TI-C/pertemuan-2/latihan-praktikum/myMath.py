def penambahan(a, b):
    tambah = a + b
    return(tambah)
PENAMBAHAN = penambahan(5, 2)
print('penjumlahan =', PENAMBAHAN)

def pengurangan(a, b):
    kurang = a - b
    return(kurang)
PENGURANGAN = pengurangan(5, 2)
print('pengurangan =', PENGURANGAN)

def perkalian(a, b):
    kali = a * b
    return(kali)
PERKALIAN = perkalian(5, 2)
print('perkalian =', PERKALIAN)

def pembagian(a, b):
    if b == 0:
        print('Pembagian tidak dapat dilakukan karena pembagi bernilai 0')
    else:
        bagi = a / b
        return(bagi)
PEMBAGIAN = pembagian(5, 2)
print('pembagian =', PEMBAGIAN)

def modulus(a, b):
    sisa_hasil_bagi = a % b
    return(sisa_hasil_bagi)
MODULUS = modulus(5, 2)
print('modulus =', MODULUS)


n = 5
fibon = []
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(n):
    fibon.append(fibonacci(n-i))
fibon.sort()
print(fibon)