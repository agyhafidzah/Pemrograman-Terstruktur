def maks(*semuaData):
    max = semuaData[0]
    for angka in semuaData:
        if(angka > max):
            max = angka
    return max

#contoh soal mencari nilai angka max dari kumpulan data
print(maks(-2,0,8,-30,10))
