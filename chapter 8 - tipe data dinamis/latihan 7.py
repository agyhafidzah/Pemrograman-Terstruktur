def harga(semua):
    data =list(semua.values())
    mahal = max(data)
    for key,value in semua.items():
        if value == mahal:
            return key
                

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('buah dengan harga satuan paling mahal adalah:')
print(harga(buah))
