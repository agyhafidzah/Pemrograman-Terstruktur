def sum(*semuaData):
    total = 0
    for angka in semuaData:
        total += angka
    return total

#contoh penjumlahan angka-angka dalam semuaData
print(sum(1,0,0,2,4))
