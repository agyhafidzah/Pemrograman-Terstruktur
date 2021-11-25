sayur = ['BAYAM', 'KANGKUNG', 'WORTEL', 'SELADA']
print(sayur)

print('MENU:')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur\n')
print('ket: penulisan harus kapital')
print('pilihan anda:', end='')
pilihan = str(input())

if pilihan == 'A':
    print('\ndata yang akan dihapus: ', end='')
    hapus = str(input())
    if hapus in sayur:
        nomor = sayur.index(hapus)
        del sayur [nomor]
        print(sayur)
    elif hapus not in sayur:
       print('nama sayur tidak ditemukan dalam data')
elif pilihan == 'B':
    print('\ndata yang akan ditambahkan: ', end='')
    tambah = str(input())
    if tambah not in sayur:
        sayur.append(tambah)
        print(sayur)
    elif tambah in sayur:
        print('nama sayur sudah terdapat dalam data')
elif pilihan == 'C':
    print(sayur)
else:
    print('tidak ada di opsi menu')

print('\nlagi y/n?', end='')
jawab = str(input())
while jawab == 'Y':
    print('MENU:')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur\n')
    print('ket: penulisan harus kapital')
    print('pilihan anda:', end='')
    pilihan = str(input())
    if pilihan == 'A':
        print('\ndata yang akan dihapus: ', end='')
        hapus = str(input())
        if hapus in sayur:
            nomor = sayur.index(hapus)
            del sayur [nomor]
            print(sayur)
        elif hapus not in sayur:
            print('nama sayur tidak ditemukan dalam data')
        print('\nlagi y/n?', end='')
        jawab = str(input())
    elif pilihan == 'B':
        print('\ndata yang akan ditambahkan: ', end='')
        tambah = str(input())
        if tambah not in sayur:
            sayur.append(tambah)
            print(sayur)
        elif tambah in sayur:
            print('nama sayur sudah terdapat dalam data')
        print('\nlagi y/n?', end='')
        jawab = str(input())
    elif pilihan == 'C':
        print(sayur)
        print('\nlagi y/n?', end='')
        jawab = str(input())
    else:
        print('tidak ada di opsi menu')
        print('lagi y/n?', end='')
        jawab = str(input())
while jawab == 'N':
    print('data terbaru :', sayur)
    break
