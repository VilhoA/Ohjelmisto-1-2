# muistilista
    # pii~4n/N
    # x**2+y**2<1
    #N= pisteiden lukumäärä
    #n= pisteiden määrä ympyrän sisällä
    #n= N * math.pi /4

import random
N= int(input('syötä lukuparien määrä: '))

kierrokset= 0
n= 0

while kierrokset <N:
    x = (random.uniform (-1.0, 1.0))
    y = (random.uniform(-1.0, 1.0))

    if (x ** 2 + y ** 2) < 1:
        n += 1


    kierrokset += 1

print (('piin likiarvo on: ') + str(4 * n / N))

#ohjelma toimii ilmeisesti oikein sillä mitä suurempi määrä pisteitä annetaan sitä lähempänä ollaan piin likiarvoa