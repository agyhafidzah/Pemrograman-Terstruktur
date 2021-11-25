#c merupakan sisi miring segitiga
#rumus pythagoras adalah kuadrat sisi miring harus sama dengan penjumlahan
#kuadrat 2 sisi segitiga
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

def isPythagoras(a,b,c):
    if c*c == (a*a)+(b*b):
        print(True)
    else:
        print(False)


isPythagoras(a,b,c)
