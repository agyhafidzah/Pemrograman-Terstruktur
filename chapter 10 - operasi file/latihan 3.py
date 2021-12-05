file = open('d:\phyton2.txt', 'r')
isi = file.readlines()

mylist = ['nim', 'nama','alamat']
hasil = []
for data in isi:
    data2 = data.split('|')
    data3 = data2[2].split('\n')
    data4 = [data2[0], data2[1], data3[0]]
    data5 = dict(zip(mylist, data4))
    hasil.append(data5)

print('\n', hasil)

