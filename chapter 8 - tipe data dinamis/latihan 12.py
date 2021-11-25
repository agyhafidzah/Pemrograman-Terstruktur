#data list buah dan harga
buah = {'apel' : '5000', 'jeruk' : '8500', 'mangga' : '7800', 'duku' : '6500'}
gabung = list(buah.items())
kunci = list(buah.keys())
value = list(buah.values())

listApel = []
listJeruk = []
listMangga = []
listDuku = []


print('Menu:')
print('A. Tanbah data buah')
print('B. Beli buah')
print('C. Hapus buah dalam daftar\n')
print('Pilihan menu :', end='')
pilihan = str(input())

while pilihan == 'A':
    print('masukkan nama buah:' , end='')
    tambah = str(input())
    if tambah in kunci:
        print('nama buah sudah ada dalam daftar')
    elif tambah not in kunci:
        print('masukkan harga satuan:', end='')
        hargabaru = str(input())
        print('\nDatabuah:\n')
        for i,j in gabung:
            print('-', i , '(Harga Rp', j, ')')
        print('-' , tambah , '(Harga Rp', hargabaru, ')')
        break
if pilihan == 'B':
    print('\nDaftar buah')
    print(buah)
    print('\nket = penulisan menggunakan huruf kecil')
    print('Nama buah yang dibeli :', end='')
    nama = str(input())
    print('Berapa Kg             :', end='')
    jumlah = int(input())
    if nama == 'apel':
        harga1 = jumlah*5000
        listApel.append(harga1)
    elif nama == 'jeruk':
        harga2 = jumlah*8500
        listJeruk.append(harga2)
    elif nama == 'mangga':
        harga3 = jumlah*7800
        listMangga.append(harga3)
    elif nama == 'duku':
        harga4 = jumlah*6500
        listDuku.append(harga4)

    print('\nbeli buah yang lain(y/n)?', end='')
    jawab = str(input())
    while jawab == 'y':
        print('\nNama buah yang dibeli :', end='')
        nama = str(input())
        print('Berapa Kg             :', end='')
        jumlah = int(input())
        if nama == 'apel':
            harga1 = jumlah*5000
            listApel.append(harga1)
        elif nama == 'jeruk':
            harga2 = jumlah*8500
            listJeruk.append(harga2)
        elif nama == 'mangga':
            harga3 = jumlah*7800
            listMangga.append(harga3)
        elif nama == 'duku':
            harga4 = jumlah*6500
            listDuku.append(harga4)
        print('\nbeli buah yang lain(y/n)?', end='')
        jawab = str(input())
    while jawab == 'n':
        print('--------------------------------')
        print('Total harga           :', end='')
        jumlah1 = sum(listApel)
        jumlah2 = sum(listJeruk)
        jumlah3 = sum(listMangga)
        jumlah4 = sum(listDuku)
        total = jumlah1+jumlah2+jumlah3+jumlah4
        print('Rp.' + str(total))
        break
while pilihan == 'C':
    print('masukkan nama buah yang akan dihapus:', end='')
    hapus = str(input())
    if hapus not in buah:
        print('buah tidak ditemukan dalam daftar')
    if hapus in buah:
        del buah[hapus]
        print('\ndaftar terbaru:', buah)
        break
        
while pilihan != 'A':
    if pilihan != 'B':
        if pilihan != 'C':
            print('tidak ada dalam opsi')
            break
