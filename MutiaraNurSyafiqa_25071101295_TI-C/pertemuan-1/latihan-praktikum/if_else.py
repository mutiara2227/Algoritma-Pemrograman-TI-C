#Phyton If

usia = 25
if usia >= 18:
    print('sudah dewasa')
    print('bisa mencoblos')
    print('memiliki hak hukum penuh')


#Phyton Elif

day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")


#Phyton Else

nilai = 80
if nilai >= 75:
    print('tidak remedial')
else:
    print('remedial')


#Shorthand If

umur = 18
if umur >= 17: print('Memenuhi umur untuk membuat KTP')


#Logical Operators

username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")


#Nested If

jam = 13.00
panas_terik = True
if jam >= 12.00:
    if panas_terik:
        print('Hari sudah siang')


#Pass Statement
a = 5
b = 2
if a > b:
    pass
print('selesai')
