def rerata(*semuaData):
    jumlah = 0
    for angka in semuaData:
        jumlah = jumlah+1
    return sum(semuaData)/jumlah

#contoh menghitung rata-rata dari beberapa bilangan
print(rerata(1,0,0,2,4))
