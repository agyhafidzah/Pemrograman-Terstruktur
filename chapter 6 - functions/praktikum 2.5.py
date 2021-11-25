def luasSegitiga(a,t):
    luas = a*t/2
    return luas
def totalLuas(a,b):
    jumlah = a+b
    return jumlah

alas = 10
tinggi = 20
print('Luas segitiga dengan alas', alas,
      ' dan tinggi', tinggi,
      'adalah', luasSegitiga(alas,tinggi))
luasA = luasSegitiga(alas,tinggi)

alas = 15
tinggi = 45
print('Luas segitiga dengan alas', alas,
      ' dan tinggi', tinggi,
      'adalah', luasSegitiga(alas,tinggi))
luasB = luasSegitiga(alas,tinggi)

print('jadi total luas kedua segitiga tersebut adalah ', totalLuas(luasA,luasB))


