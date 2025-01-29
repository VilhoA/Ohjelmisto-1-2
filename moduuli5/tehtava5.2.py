lista = []

while True:
    numero = input('syötä lukema tai lopeta painamalla enter: ')

    if numero == '':
        break

    lista.append (int(numero))

lista.sort(reverse = True)
print (lista)

#print ('suurimmat 5 lukuasi suurimmasta pienimpään: ', (lista[:5]))
print (f'suurimmat 5 lukuasi suurimmasta pienimpään: {lista[:5]}')

