from datetime import *

file = open('d:\contoh17.txt', 'r')
sekarang = datetime.date(datetime.now())

print('Masukkan kode :', end='')
kode = input()


gabungkode = []
gabungnama = []
gabungjudul = []
gabungpinjam = []
gabungkembali = []
kembali = []
isi = file.readlines()

for data in isi:
    data2 = data.split('|')
    gabungkode.append(data2[0])
    gabungnama.append(data2[1])
    gabungjudul.append(data2[2])
    gabungpinjam.append(data2[3])
    gabungkembali.append(data2[4])

if kode in gabungkode:
    index = gabungkode.index(kode)
    data3 = gabungkembali[index]
    data4 = str(data3)
    a = sekarang.day
    b = sekarang.month
    c = sekarang.year
    d = data4.split('-')
    print('\nData Peminjaman Buku')
    print('Kode Member               :', kode)
    print('Nama Member               :', gabungnama[index])
    print('Judul Buku                :', gabungjudul[index])
    print('Tanggal Mulai Peminajaman :', gabungpinjam[index])
    print('Tanggal Maks Peminjaman   :', gabungkembali[index] , end='')
    print('Tanggal Pengembalian      :', str(sekarang))
    print('Terlambat                 :',end ='')
    if c <= int(d[0]):
        if b <= int(d[1]):
            if a <= int(d[0]):
                e = 0
                print('', e)
    else:
        print((a-int(d[2])), 'hari', (b-int(d[1])), 'bulan', (c-int(d[0])), 'tahun')
        e = (a-int(d[2]))+ (b-int(d[1]))*30+ (c-int(d[0]))*365
    print('Denda                     :', 'Rp', e*2000)
else:
    print('data member tidak ditemukan')

file.close()
