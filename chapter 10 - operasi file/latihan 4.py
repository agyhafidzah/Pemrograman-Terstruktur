file = open('d:\contoh.txt', 'r')

print('Masukkan NIM :', end='')
nim = input()

gabungnim = []
gabungnama = []
gabungalamat = []
isi = file.readlines()

for data in isi:
    data2 = data.split('|')
    gabungnim.append(data2[0])
    gabungnama.append(data2[1])
    data3 = data2[2].split('\n')
    gabungalamat.append(data3[0])

if nim in gabungnim:
    index = gabungnim.index(nim)
    print('\ndata mahasiswa')
    print('NIM     :', nim)
    print('nama    :', gabungnama[index])
    print('alamat  :', gabungalamat[index])
else:
    print('Data mahasiswa tidak ditemukan')

file.close()


