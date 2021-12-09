from datetime import *

data =[]
print('masukkan kode Member : ', end='')
kode = input()
data.append(kode)
print('masukkan nama Member : ', end='')
nama = input()
data.append(nama)
print('masukkan judul buku  : ', end='')
judul = input()
data.append(judul)
sekarang =  datetime.date(datetime.now())
data.append(str(sekarang))
selesai = sekarang + timedelta(days=7)
data.append(str(selesai))

gabung ='|'.join(data)

file = open('d:\contoh17.txt', 'a+')
file.write(gabung)
file.write('\n')

print('lagi(y/n)?')
jawab = input()
while jawab == 'y':
    data =[]
    print('masukkan kode Member : ', end='')
    kode = input()
    data.append(kode)
    print('masukkan nama Member : ', end='')
    nama = input()
    data.append(nama)
    print('masukkan judul buku  : ', end='')
    judul = input()
    data.append(judul)
    sekarang =  datetime.date(datetime.now())
    data.append(str(sekarang))
    selesai = sekarang + timedelta(days=7)
    data.append(str(selesai))

    gabung ='|'.join(data)

    file = open('d:\contoh17.txt', 'a+')
    file.write(gabung)
    file.write('\n')
    print('lagi(y/n)?')
    jawab = input()
while jawab == 'n':
    break

file.seek(0,0)
isi = file.read()
print(isi)

file.close()
