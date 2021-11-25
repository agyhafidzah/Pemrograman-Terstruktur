import random
import sys
import time

nyawa = 3
skor = 0

print('Menu pilihan level:')
print('1. Level 1(Penjumlahan)')
print('2. Level 2(Pengurangan)')
print('3. Level 3(Perkalian)')
print('4. Exit')
print('Pilih nomor pilihan:')
pilihan = int(input())

while (pilihan == 1):
    x1 = random.randint(-100, 100)
    y1 = random.randint(-100, 100)
    z1 = x1+y1
    print ('hasil penjumlahan antara (' + str(x1) + ')+(' + str(y1) + ') adalah')
    jawab1 = int(input())
    if (jawab1 == z1):
        nyawa = nyawa
        skor = skor+2
        print ('yeayy selamat!! kamu benar' + '(lives:' + str(nyawa) + ')')
    elif (jawab1 != z1):
        nyawa = nyawa-1
        skor = skor-2
        print ('yahh kamu salah, coba lagi yuk' + '(lives:' + str(nyawa) + ')')
        if (nyawa <= 0):
            print ('hehe tapi sayang kesempatan kamu sudah habis!! skor kamu adalah '+ str(skor) + '(lives:' + str(nyawa) + ')')
            print ('GAME OVER')
            break
while (pilihan == 2):
    x2 = random.randint(-100, 100)
    y2 = random.randint(-100, 100)
    z2 = x2-y2
    print ('hasil pengurangan antara (' + str(x2) + ')-(' + str(y2) + ') adalah')
    jawab1 = int(input())
    if (jawab1 == z2):
        nyawa = nyawa
        skor = skor+2
        print ('yeayy selamat!! kamu benar' + '(lives:' + str(nyawa) + ')')
    elif (jawab1 != z2):
        nyawa = nyawa-1
        skor = skor-2
        print ('yahh kamu salah, coba lagi yuk' + '(lives:' + str(nyawa) + ')')
        if (nyawa <= 0):
            print ('hehe tapi sayang kesempatan kamu sudah habis!! skor kamu adalah '+ str(skor) + '(lives:' + str(nyawa) + ')')
            print ('GAME OVER')
            break
while (pilihan == 3):
    x3 = random.randint(-100, 100)
    y3 = random.randint(-100, 100)
    z3 = x3*y3
    print ('hasil perkalian antara (' + str(x3) + ')x(' + str(y3) + ') adalah')
    jawab1 = int(input())
    if (jawab1 == z3):
        nyawa = nyawa
        skor = skor+2
        print ('yeayy selamat!! kamu benar' + '(lives:' + str(nyawa) + ')')
    elif (jawab1 != z3):
        nyawa = nyawa-1
        skor = skor-2
        print ('hehe kamu salah, coba lagi yuk' + '(lives:' + str(nyawa) + ')')
        if (nyawa <= 0):
            print ('aduhh tapi sayang kesempatan kamu sudah habis!! skor kamu adalah '+ str(skor) + '(lives:' + str(nyawa) + ')')
            print ('GAME OVER')
            break
if (pilihan == 4):
    print ('Good Bye!! and see u')
    time.sleep(1)
    sys.exit()
if (pilihan != 1 and pilihan!= 2 and pilihan!= 3 and pilihan!= 4):
    print('Maaf pilihan Anda salah')
    sys.exit()



      
