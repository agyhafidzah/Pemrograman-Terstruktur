#data list buah dan harga
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
kunci = list(buah.items())

listApel = []
listJeruk = []
listMangga = []
listDuku = []

print('daftar buah dan harga:')
print(kunci)
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
