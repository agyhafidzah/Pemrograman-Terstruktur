def starFormation1(n):
    i = 3
    while(i < n):
        j = 3
        while(j <= i):
            print('*', end='')
            j += 1
        print('')
        i += 1

def starFormation2(n):
    i = 4
    while (n > i):
        j = 4
        while(j < n):
            print('*', end='')
            j += 1
        print('')
        n -= 1

n = 7
starFormation1(n)
starFormation2(n)

