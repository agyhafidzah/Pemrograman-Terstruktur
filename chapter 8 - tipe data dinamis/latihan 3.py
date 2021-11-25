print('masukkan jumlah siswa :' , end='')
jumlahN = int(input())

n = 0
data =[]
while jumlahN >= 0:
    if n == jumlahN:
        print('\nlist nama mahasiswa: ')
        break
    if n != jumlahN :
        print ('Masukkan nama siswa :')
        nama = str(input())
        data.append(nama)
        data.sort() 
        n = n+1
for nama in data:
    print(nama, '(', len(nama), 'karakter)')
