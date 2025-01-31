luvut = []

while True:
    useri= (input('syötä kokonaisluku tai lopeta painamalla enter: '))
    if useri == '':
        break
    luvut.append (int(useri))




def lasku(summa):
    tulos = 0
    for lasku in summa:
        tulos += lasku
    return tulos

print(f'lukujen summa on: {lasku(luvut)}')
