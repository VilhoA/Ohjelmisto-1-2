import random
maksimi = int(input('syötä nopan suurin tahko: '))

def noppa (tahkot):
    return random.randint(1, tahkot)

while True:
    tulos = noppa(maksimi)
    print (tulos)
    if tulos == (maksimi):
        break





