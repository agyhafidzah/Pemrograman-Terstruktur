from datetime import*

def diffDate(x):
    sekarang =  datetime.date(datetime.now())
    data = str(sekarang)
    a = datetime.strptime(x, '%Y-%m-%d')
    b = datetime.strptime(data, '%Y-%m-%d')
    if a >= b :
        c = a-b
    elif a <= b :
        c = b-a
    print(c.days)
    
        

diffDate('2021-12-30')
