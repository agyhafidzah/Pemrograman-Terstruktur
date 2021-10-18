import random 

print('Halo, aku robot, aku telah memilih bilangan bulat secara acak antara 0-100. Tebak berapa angka yang kupilih!!')

soal = random.randint(1,100)
while soal > 0:
    print('berapa tebakanmu? >~<')
    jawaban = int(input())
    if jawaban > soal:
        print('aduhh.. tebakanmu terlalu besar')
    if jawaban < soal:
        print('yahh.. tebakanmu terlalu kecil')
    if jawaban == soal:
        print('yeayy akhirnya kamu berhasil!! tebakanmu benar')
        break
    
