file = open('d:\contoh2.txt', 'r')
file2 = open('d:\contoh6.txt', 'a+')

isi = file.readlines()

#memecah data menggunakan split
bil1=[]
bil2=[]
for data in isi:
    data2 = data.split('|')
    bil1.append(data2[0])
    data3 = data2[1].split('\n')
    bil2.append(data3[0])

#hasil penjumlahan bilangan 1 dan bilangan 2
for i in range(len(bil1)):
    x = int(bil1[i])
    y = int(bil2[i])
    jumlah = x+y
    file2.write(str(jumlah))
    file2.write('\n')

file2.seek(0,0)
isi2 = file2.read()
print(isi2)
    
file.close()
file2.close()
