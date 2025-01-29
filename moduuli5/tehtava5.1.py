import random
lista = []
nopat = int(input('syötä noppien määrä: '))

while nopat > 0:
    arpa = random.randint(1,6)
    print(arpa)
    lista.append(arpa)
    nopat -= 1

luku = 0
for n in lista:
    luku = luku + n
print ('arvottujen noppien summa: ' + str(luku))




