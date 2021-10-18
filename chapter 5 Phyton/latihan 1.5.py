print('Ketik dengan huruf kapital')

#berikut ini adalah gaji bersih dan potongan dengan rumus
#potongan = gaji pokok*potongan/100
#gaji bersih = gaji pokok - potongan


gajiPokokA = 10000000
potonganA = 2.5
hasilpotonganA = gajiPokokA*potonganA/100
tunjanganIstriA = gajiPokokA*10/100
tunjanganAnakA = gajiPokokA*5/100

gajiPokokB = 8500000
potonganB = 2.0
hasilpotonganB =  gajiPokokB*potonganB/100
tunjanganIstriB = gajiPokokB*10/100
tunjanganAnakB = gajiPokokB*5/100

gajiPokokC = 7000000
potonganC = 1.5
hasilpotonganC =  gajiPokokC*potonganC/100
tunjanganIstriC = gajiPokokC*10/100
tunjanganAnakC = gajiPokokC*5/100

gajiPokokD = 5500000
potonganD = 1.0
hasilpotonganD = gajiPokokD*potonganD/100
tunjanganIstriD = gajiPokokD*10/100
tunjanganAnakD = gajiPokokD*5/100

print('masukkan kode karyawan : ')
kode = int(input())
print('masukkan nama karyawan : ')
nama = str(input())
print('masukkan golongan : ')
golongan = str(input())
print('masukkan status :')
print('ket: ketik 1 apabila sudah menikah')
print('     ketik 2 apabila belum menikah')
status = str(input())
if (status == '1'):
    statusnikah = 'Sudah menikah'
else:
    statusnikah = 'Belum menikah'
print('masukkan jumlah anak : ')
print('ket: masukkan angka 0 apabila belum menikah')
anak = int(input())

print('===============================================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('---------------------------------------------------------------')
print('Nama karyawan:' + str(nama) + '(Kode):' + str(kode))
print('Golongan:' + golongan)
print('Status menikah:' + statusnikah)
print('Jumlah anak:' + str(anak))
print('---------------------------------------------------------------')

if (golongan == 'A'):
    print('Gaji Pokok:' + str(gajiPokokA))
if (golongan == 'B'):
    print('Gaji Pokok:' + str(gajiPokokB))
if (golongan == 'C'):
    print('Gaji Pokok:' + str(gajiPokokC))
if (golongan == 'D'):  
    print('Gaji Pokok:' + str(gajiPokokD))
if (status == '1'):
    if (golongan == 'A'):
        print('Tunjangan suami/istri:' + 'Rp' + str(tunjanganIstriA))
    if (golongan == 'B'):
        print('Tunjangan suami/istri:' + 'Rp' + str(tunjanganIstriB))
    if (golongan == 'C'):
        print('Tunjangan suami/istri:' + 'Rp' + str(tunjanganIstriC))
    if (golongan == 'D'):  
        print('Tunjangan suami/istri:' + 'Rp' + str(tunjanganIstriD))
if (status == '2'):
    tunjanganIstriA = 0
    tunjanganIstriB = 0
    tunjanganIstriC = 0
    tunjanganIstriD = 0


if (anak > 0):
    jumlahTunjanganAnakA = tunjanganAnakA*anak
    jumlahTunjanganAnakB = tunjanganAnakB*anak
    jumlahTunjanganAnakC = tunjanganAnakC*anak
    jumlahTunjanganAnakD = tunjanganAnakD*anak
    if (golongan == 'A'):
        print('Tunjangan anak:' + 'Rp' + str(jumlahTunjanganAnakA))
    if (golongan == 'B'):
        print('Tunjangan anak:' + 'Rp' + str(jumlahTunjanganAnakB))
    if (golongan == 'C'):
        print('Tunjangan anak:' + 'Rp' + str(jumlahTunjanganAnakC))
    if (golongan == 'D'):  
        print('Tunjangan anak:' + 'Rp' + str(jumlahTunjanganAnakD))
if (anak <= 0):
    jumlahTunjanganAnakA = 0
    jumlahTunjanganAnakB = 0
    jumlahTunjanganAnakC = 0
    jumlahTunjanganAnakD = 0

    
print('---------------------------------------------------------------')

gajiKotorA = gajiPokokA+tunjanganIstriA+jumlahTunjanganAnakA
gajiKotorB = gajiPokokB+tunjanganIstriB+jumlahTunjanganAnakB
gajiKotorC = gajiPokokC+tunjanganIstriC+jumlahTunjanganAnakC
gajiKotorD = gajiPokokD+tunjanganIstriD+jumlahTunjanganAnakD

if (golongan == 'A'):
    print('Gaji Kotor:' + 'Rp' + str(gajiKotorA))
    print('Potongan(2.5%):' + 'Rp' + str(hasilpotonganA))
if (golongan == 'B'):
    print('Gaji Kotor:' + 'Rp' + str(gajiKotorB))
    print('Potongan(2.0%):' + 'Rp' + str(hasilpotonganB))
if (golongan == 'C'):
    print('Gaji Kotor:' + 'Rp' + str(gajiKotorC))
    print('Potongan(1.5%):' + 'Rp' + str(hasilpotonganC))
if (golongan == 'D'):  
    print('Gaji Kotor:' + 'Rp' + str(gajiKotorD))
    print('Potongan(1.0%):' + 'Rp' + str(hasilpotonganD))
    
print('---------------------------------------------------------------')

gajiBersihA = gajiKotorA-hasilpotonganA
gajiBersihB = gajiKotorB-hasilpotonganB
gajiBersihC = gajiKotorC-hasilpotonganC
gajiBersihD = gajiKotorD-hasilpotonganD

if (golongan == 'A'):
    print('Gaji Bersih:' + 'Rp' + str(gajiBersihA))
if (golongan == 'B'):
    print('Gaji Bersih:' + 'Rp' + str(gajiBersihB))
if (golongan == 'C'):
    print('Gaji Bersih:' + 'Rp' + str(gajiBersihC))
if (golongan == 'D'):  
    print('Gaji Bersih:' + 'Rp' + str(gajiBersihD))

    






