joukko = set()

while True:
    useri = input('syötä nimi:')


    if useri=='':
        break

    if useri in joukko:
        print ('aiemmin syötetty nimi')
    else:
        print('uusi nimi')

    joukko.add(useri)

print("")

print ("syöttämäsi nimet:")
for n in joukko:
    print (n)