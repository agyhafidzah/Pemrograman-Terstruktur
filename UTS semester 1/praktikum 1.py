#berikut ini adalah kode program untuk menentukan
#tahun yang diinputkan kabisat/bukan kabisat
print('Masukkan Tahun:')
soal = int(input())

syarat1 = soal%400
syarat2 = soal%100
syarat3 = soal%4

if (syarat1 == 0):
    print('Tahun ' + str(soal) + ' merupakan TAHUN KABISAT')
elif(syarat1 != 0 and syarat2 == 0):
    print('Tahun ' + str(soal) + ' bukan merupakan TAHUN KABISAT')
elif(syarat1 != 0 and syarat2 != 0 and syarat3 == 0):
    print('Tahun ' + str(soal) + ' merupakan TAHUN KABISAT')
else:
    print('Tahun ' + str(soal) + ' bukan merupakan TAHUN KABISAT')
