#data list buah dan harga
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
kunci = list(buah.items())

print('daftar buah dan harga:')
print(kunci)
print('\nNama buah yang dibeli :', end='')
nama = str(input())
print('Berapa Kg             :', end='')
jumlah = int(input())
print('--------------------------------')
print('Total harga           :', end='')
if nama == 'apel':
    harga1 = jumlah*5000
    print('Rp.' + str(harga1))
elif nama == 'jeruk':
    harga2 = jumlah*8500
    print('Rp.' + str(harga2))
elif nama == 'mangga':
    harga3 = jumlah*7800
    print('Rp.' + str(harga3))
elif nama == 'duku':
    harga4 = jumlah*6500
    print('Rp.' + str(harga4))
    
