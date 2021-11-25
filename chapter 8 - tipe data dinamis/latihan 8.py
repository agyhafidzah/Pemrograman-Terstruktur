def rerata(semua):
    sum = 0
    jumlah = 0
    for i in semua.values():
        sum = sum+i
        jumlah = jumlah+1
        average = sum/jumlah
    return average

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('harga rata-rata buah adalah:', end=' ')
print(rerata(buah))
