import random 

print('Halo, aku robot, aku telah memilih bilangan bulat secara acak antara 0-100. Tebak berapa angka yang kupilih!!')

score = 100
soal = random.randint(1,100)
while soal > 0:
    print('berapa tebakanmu? >~<')
    jawaban = int(input())
    score = score - 2
    if score <= 0:
        print('score kamu sudah 0 nih, kamu kalah!')
        break
    elif jawaban > soal:
        print('aduhh.. tebakanmu terlalu besar')
    elif jawaban < soal:
        print('yahh.. tebakanmu terlalu kecil')
    elif jawaban == soal:
        print('yeayy akhirnya kamu berhasil!! tebakanmu benar')
        break
    
print ('score kamu adalah:' + str(score))
