file = open("d:/dataa.txt", "r")

try:
    sum = 0
    for dataa in file:
        sum = sum + int(dataa)
    print(sum)
except ValueError:
    print('jenis data tidak sama')
