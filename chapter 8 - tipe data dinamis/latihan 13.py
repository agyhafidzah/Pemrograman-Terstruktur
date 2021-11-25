def tertinggi(semua):
    gabungan =[]
    for data in semua:
        mid = data['mid']
        uas = data['uas']
        nilai = (mid + 2*uas)/3
        gabungan = gabungan + [round(nilai, 1)]

    index= []
    i = 0
    for nilai in gabungan:
        tertinggi = max(gabungan)
        if nilai == tertinggi:
            index = index+[i]
        i = i+1

    for i in index:
        print('\nberikut adalah nama mahasiswa dengan nilai akhir tertinggi:')
        print('Nama :', semua[i]['nama'], '(Nim :' + semua[i]['nim']+')',
              'dengan nilai akhir', gabungan[i])

    
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

tertinggi(nilaiMhs)
