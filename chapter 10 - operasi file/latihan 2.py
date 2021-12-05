data =[]
print('masukkan NIM: ', end='')
nim = input()
data.append(nim)
print('masukkan nama Mhs: ', end='')
nama = input()
data.append(nama)
print('masukkan alamat: ', end='')
alamat = input()
data.append(alamat)

gabung ='|'.join(data)

file = open('d:\contoh.txt', 'a+')
file.write(gabung)
file.write('\n')

print('lagi(y/n)?')
jawab = input()
while jawab == 'y':
    data =[]
    print('masukkan NIM: ', end='')
    nim = input()
    data.append(nim)
    print('masukkan nama Mhs: ', end='')
    nama = input()
    data.append(nama)
    print('masukkan alamat: ', end='')
    alamat = input()
    data.append(alamat)

    gabung ='|'.join(data)

    file = open('d:\contoh.txt', 'a+')
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
