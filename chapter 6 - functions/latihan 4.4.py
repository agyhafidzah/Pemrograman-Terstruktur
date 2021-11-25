def min(*semuaData):
    min = semuaData[0]
    for angka in semuaData:
        if(angka < min):
            min = angka
    return min

#contoh soal mencari nilai angka min dari kumpulan data
print(min(-2,0,8,-30,10))
