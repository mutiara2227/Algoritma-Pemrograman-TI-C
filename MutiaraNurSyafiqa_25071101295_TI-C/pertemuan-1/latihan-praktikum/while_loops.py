#1 (Eksekusi perintah selama kondisinya terpenuhi/True)
i = 1 #Pendefinisian variabel indeks
while i < 6:
  print(i)
  i += 1

#2 (Break Statement)
j = 1
while j < 8:
    print(j)
    if j == 5:
        break #menghentikan loop walaupun True
    j += 1
print('\n')

#3 (Continue Statement)
i = 0
while i < 8:
    i += 1
    if i == 5:
        continue #memberhentikan iteration saat ini & melanjutkan selanjutnya
    print(i)

#4 (Else Statement)
i = 1
while i < 8:
    print(i)
    i += 1
else: 
    print('i sudah melebihi 8')
