print('Ketik dengan huruf kapital')

#berikut ini adalah gaji bersih dan potongan dengan rumus
#potongan = gaji pokok*potongan/100
#gaji bersih = gaji pokok - potongan


gajiPokokA = 10000000
potonganA = 2.5
hasilpotonganA = gajiPokokA*potonganA/100
gajiBersihA = gajiPokokA-hasilpotonganA
gajiPokokB = 8500000
potonganB = 2.0
hasilpotonganB =  gajiPokokB*potonganB/100
gajiBersihB =  gajiPokokB-hasilpotonganB
gajiPokokC = 7000000
potonganC = 1.5
hasilpotonganC =  gajiPokokC*potonganC/100
gajiBersihC = gajiPokokC-hasilpotonganC
gajiPokokD = 5500000
potonganD = 1.0
hasilpotonganD = gajiPokokD*potonganD/100
gajiBersihD = gajiPokokD-hasilpotonganD

print('masukkan kode karyawan : ')
kode = int(input())
print('masukkan nama karyawan : ')
nama = str(input())
print('masukkan golongan : ')
golongan = str(input())
print('===============================================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('---------------------------------------------------------------')
print('Nama karyawan:' + str(nama) + '(Kode):' + str(kode))
print('Golongan:' + golongan)
print('---------------------------------------------------------------')
if (golongan == 'A'):
    print('Gaji Pokok:' + str(gajiPokokA))
    print('Potongan(2.5%):' + 'Rp' + str(hasilpotonganA))
if (golongan == 'B'):
    print('Gaji Pokok:' + str(gajiPokokB))
    print('Potongan(2.0%):' + 'Rp' + str(hasilpotonganB))
if (golongan == 'C'):
    print('Gaji Pokok:' + str(gajiPokokC))
    print('Potongan(1.5%):' + 'Rp' + str(hasilpotonganC))
if (golongan == 'D'):  
    print('Gaji Pokok:' + str(gajiPokokD))
    print('Potongan(1.0%):' + 'Rp' + str(hasilpotonganD))
print('---------------------------------------------------------------')
if (golongan == 'A'):
    print('Gaji Bersih:' + 'Rp' + str(gajiBersihA))
if (golongan == 'B'):
    print('Gaji Bersih:' + 'Rp' + str(gajiBersihB))
if (golongan == 'C'):
    print('Gaji Bersih:' + 'Rp' + str(gajiBersihC))
if (golongan == 'D'):  
    print('Gaji Bersih:' + 'Rp' + str(gajiBersihD))







