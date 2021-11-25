def faktorial(n):
    hasil = n
    while (n == 1):
        hasil = 1
        return hasil
    while (n == 0):
        hasil = 1
        return hasil
    while(n > 1):
        n -= 1
        hasil = hasil*n
    return hasil

n = int(input('n = '))
print(faktorial(n))
