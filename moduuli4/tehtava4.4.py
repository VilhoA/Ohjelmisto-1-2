from random import randint

numero= randint(1,10)

while True:
    arvaus= int(input('syötä arvaus: '))
    if arvaus > numero:
        print ('liian suuri arvaus')
    elif arvaus < numero:
        print ('liian pieni arvaus')
    else:
        print ('oikein')
        break



