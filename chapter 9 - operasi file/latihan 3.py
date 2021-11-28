def formasi(n):
    selisih = 2*n-1
    atas = n//2+1
    bawah = n//2
    for i in range(atas):
        print(('*'*(2*i+1)).center(selisih))
    for i in range(1, bawah+1):
        print(((i*'')+((bawah-i+1)*'*')+((bawah-i)*'*')).center(selisih))
            
formasi(7)
