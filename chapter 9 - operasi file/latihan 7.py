mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('==============================================================')
print('NIM       NAMA MAHASISWA       TGL LAHIR      TEMPAT LAHIR')
print('--------------------------------------------------------------')

for i in range(len(mhs)):
    hasil = mhs[i].split(':')
    print((hasil[0]).ljust(10),end ='')
    print((hasil[1]).ljust(21), end ='')
    jawab = hasil[2].split('-')
    a = jawab[0]
    b = jawab[1]
    c = jawab[2]
    d = c, b, a
    data = '/'.join(d)
    print(data.ljust(15),end='')
    print(hasil[3].ljust(11))
    
print('==============================================================')  
