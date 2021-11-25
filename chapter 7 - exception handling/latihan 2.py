print('masukkan nama file', )
namafile = (str(input()))
try:
    file = open(namafile ,"r")
    print('data yang mau ditambahkan:', )
    file = open(namafile ,"a")
    file.write(str(input()))
    print('lagi (y/n): ')
    data =(input())
    while data == 'y' :
        print('data yang mau ditambahkan:', )
        file = open(namafile ,"a")
        file.write(str(input()))
        print('lagi (y/n): ')
        data =(input(str()))
        if data == 'n' :
            file.close()
            break
        while data != 'y':
            print ('data harus berupa y atau n')
            print('lagi (y/n): ')
            data =(input(str()))
except FileNotFoundError:
    print ('File tidak ditemukan')
except ValueError:
    print ('jenis data tidak sama')

      
