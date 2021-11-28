import random

def shuffleString(x, n):
    myString = []
    for m in x:
        myString.append(m)
    data = []
    for i in range(n):
        hasil = ''.join(random.sample(myString, len(myString)))
        data.append(hasil)
    print(data)

shuffleString('aku', 3)
