print('masukkan nama file', )
namafile = (str(input()))
try:
    file = open(namafile ,"r")
    print('isi file', namafile, 'adalah:')
    for namafile in file:
        print (namafile)
except FileNotFoundError:
    print ('File tidak ditemukan')

