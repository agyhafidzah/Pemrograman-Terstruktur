def starFormation2(n):
    i = 0
    while (n > i):
        j = 0
        while(j < n):
            print('*', end='')
            j += 1
        print('')
        n -= 1

n = int(input('n = '))
starFormation2(n)
