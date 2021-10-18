#syarat lulus ujian
#nilai harus lebih dari atau sama dengan 60
#nilai matematika harus diatas 70

print('nilai bahasa indonesia : ')
nilaiIndonesia = int(input())
print('nilai bahasa IPA : ')
nilaiIPA = int(input())
print('nilai bahasa matematika : ')
nilaiMatematika = int(input())

if (nilaiIndonesia >=0 and nilaiIndonesia <=100 and nilaiIPA >= 0 and nilaiIPA <=100 and
    nilaiMatematika >= 0 and nilaiMatematika <=100):
    if nilaiIndonesia < 60 or nilaiIPA < 60 or nilaiMatematika <= 70:
        status = 'TIDAK LULUS'
    else:
        status = 'LULUS'
    print('Status kelulusan siswa adalah:' + status)
    if nilaiIndonesia < 60:
        print('nilai bahasa indonesia kurang dari 60')
    if nilaiIPA < 60:
        print('nilai bahasa IPA kurang dari 60')
    if nilaiMatematika <= 70:
        print('nilai matematika tidak diatas 70')
else:
    print('maaf input ada yang tidak valid')

