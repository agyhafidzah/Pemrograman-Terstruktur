file = open("d:/dataa.txt", "r")


sum = 0
for dataa in file:
    sum = sum + int(dataa)
print(sum)

