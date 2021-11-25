def starFormation1(n):
    i = 0
    while(i < n):
        j = 0
        while(j <= i):
            print('*', end='')
            j += 1
        print('')
        i += 1

n = int(input('n = '))
starFormation1(n)
