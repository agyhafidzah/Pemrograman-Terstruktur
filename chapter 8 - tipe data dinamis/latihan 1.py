print('masukkan jumlah n bilangan :' , end='')
jumlahN = int(input())

n = 0
data =[]
while jumlahN >= 0:
    if n == jumlahN:
        break
    if n != jumlahN :
        print('masukkan bilangan bulat:', end='')
        i = str(input())
        data.append(i)
        n = n+1

data.sort(reverse=True)
print('\n', data)

            
