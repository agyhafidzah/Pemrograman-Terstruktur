def kuadrat(*bil):
    data = list(bil)
    hasil = []
    for i in range(len(data)):
        kuadrat = data[i]*data[i]
        hasil.append(kuadrat)
    print('bil =', bil)
    print('hasil =', hasil)
    
kuadrat(4,5,6,9)

        
