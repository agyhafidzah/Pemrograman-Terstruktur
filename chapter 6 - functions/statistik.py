def sum(*semuaData):
    total = 0
    for angka in semuaData:
        total = total+angka
    return total

def rerata(*semuaData):
    jumlah = 0
    for angka in semuaData:
        jumlah = jumlah+1
    return sum(*semuaData)/jumlah

def maks(*semuaData):
    max = semuaData[0]
    for angka in semuaData:
        if(angka > max):
            max = angka
    return max

def min(*semuaData):
    min = semuaData[0]
    for angka in semuaData:
        if(angka < min):
            min = angka
    return min
