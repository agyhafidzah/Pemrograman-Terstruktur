ganjil =[]
genap =[]

file = open('d:/phyton1.txt', 'r')
isi = file.readlines()
for i in isi:
    data = int(i)%2
    if data == 0:
        genap.append(i)
    else:
        ganjil.append(i)

print('banyaknya bilangan ganjil:', len(ganjil))
print('banyaknya bilangan genap:', len(genap))
