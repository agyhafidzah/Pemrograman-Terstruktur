def sortStringByChar(*semua):
    data = list(semua)
    jawab = sorted(data, key=len, reverse=True)
    print('susunan baru', jawab)

sortStringByChar('jeruk', 'rambutan', 'apel')
