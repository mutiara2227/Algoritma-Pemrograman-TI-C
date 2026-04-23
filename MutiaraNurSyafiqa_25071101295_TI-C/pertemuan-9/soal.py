while True:
    try:
        n = int(input('Masukkan jumlah elemen: '))
        if n < 0:
            print('Harus bilangan non-negatif')
        else:
            break
    except:
        print('Input tidak valid!')

data = []
for i in range(n):
    while True:
        try:
            x = int(input(f'Elemen ke-{i+1}: '))
            if x < 0:
                print('Harus bilangan non-negatif')
            else:
                data.append(x)
                break
        except:
            print('Input tidak valid!')

print("Data awal:", data)





a= data.copy()
n = len(a)
for i in range(1,n):
  insert_index = i
  current_value = a.pop(i)
  for j in range(i-1, -1, -1):
    if a[j] > current_value:
      insert_index = j
  a.insert(insert_index, current_value)

print('Insertion Sort')
print('Sesudah di sort : ',a)





def quick(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    kiri = [x for x in data[1:] if x <= pivot]
    kanan = [x for x in data[1:] if x > pivot]
    return quick(kiri) + [pivot] + quick(kanan)

print('Quick Sort')
print('Sesudah di sort:', quick(data))




c = data.copy()
if len(c) > 0:
    count = [0] * (max(c) + 1)
    for x in c:
        count[x] += 1

    hasil = []
    for i in range(len(count)):
        hasil += [i] * count[i]
else:
    hasil = c

print('Counting Sort')
print('Sesudah di sort: ', hasil)