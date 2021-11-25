a = [1,5,6,10,3,6,9,11,20,12,4]
b = [7,4,15,5,6,7,1,12,5,9,8]
c = a[0:8]
d = b[2:10]

e = []
dataE =[]
for n in range(len(c)):
    dataE = c[n]+d[n]
    e.append(dataE)
print( 'e =', e)

tupleE = tuple(e)
print('nilai minimumnya adalah :', min(tupleE))
print('nilai minimumnya adalah :', max(tupleE))
print('jumlah seluruh elemen e adalah :', sum(tupleE))

