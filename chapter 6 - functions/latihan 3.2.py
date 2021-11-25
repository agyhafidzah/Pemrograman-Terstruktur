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
def C(n,m):
    return faktorial(n)/(faktorial(n-m)*faktorial(m))
def P(n,m):
    return faktorial(n)/(faktorial(n-m))

print(C(5,3))
print(P(10,7))
