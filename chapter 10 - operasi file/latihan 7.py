file = open('d:\contoh13.txt', 'r')
#penulisan isi file menggunakan huruf kapital
#contoh =   UCAC UWMC RAVJQP (baris1)
#           2                (baris2=n)
file2 = open('d:\contoh15.txt', 'a+')
isi = file.readlines()
data = isi[0].split('\n')

#ket: penulisan harus menggunakan huruf kapital
teks = data[0]
#input n harus bernilai 1-26(A-Z)
#n adalah banyak pergeseran huruf
n = int(isi[1])

final = []
for i in teks:
    hasil = ord(i)+26-n
    if hasil >= 91:
        m = hasil%90
        hasil = 64+m
    if hasil >= 33 and hasil <= 64:
        hasil = 32
    hasil2 = chr(hasil)
    final.append(hasil2)

gabung = ''.join(final)
file2.write(gabung)
file2.seek(0,0)
jawab = file2.read()
print('TEKS ASLI:', jawab)
    
file.close()
file2.close()
