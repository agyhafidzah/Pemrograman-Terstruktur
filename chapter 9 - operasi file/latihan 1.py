def ganti(teks, a, b):
    myString = []
    for n in teks:
        myString.append(n)
    data = []
    for i in teks:
        if i == a:
            jawab2 = myString.index(a)
            ganti = myString[jawab2] = b
            data.append(ganti)
        if i != a:
            data.append(i)
    hasil = ''.join(data)
    print(hasil)
            
ganti('MATEMATIKA', 'T', 'S')
