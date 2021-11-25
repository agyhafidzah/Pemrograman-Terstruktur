def dataStat(*semua):
    data = list(semua)
    for x in data:
        myTuple = tuple(data)
        dataA = sum(myTuple)
        b = max(myTuple)
        c = min(myTuple)
        a = dataA/len(myTuple)
        d = [a, b, c]
        dataD = list(d)
    print('ket: [nilai rata-rata, nilai tertinggi, nilai terendah]')
    print(dataD)

#contoh soal
dataStat(1,2,3,4,5)
