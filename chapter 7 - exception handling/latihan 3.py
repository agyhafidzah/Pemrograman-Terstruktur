print ('-------------------------')
print ('PROGRAM HITUNG RATA-RATA')
print ('-------------------------\n')

jumlah = 0
bagi = 0

while True:
    try:
        print ('masukkan bilangan bulat:')
        bil = int(input())
        jumlah = jumlah+bil
        print ('lagi(y/n)?')
        lagi = (input())
        bagi = bagi+1
        average = jumlah/bagi
        if lagi == 'y' :
            print(end='')
        elif lagi != 'n':
            print ('data harus berupa y atau n')
            print('lagi (y/n)? ')
            lagi =(input())
        elif lagi == 'n' :
            print ('\nrata-ratanya adalah:')
            print (average)
            break
    except ValueError:
        print ('jenis data tidak valid')
    except ZeroDivisionError:
        print ('tidak boleh pembagian dengan nol')
    
    
