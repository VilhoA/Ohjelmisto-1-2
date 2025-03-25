import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kiihdyta(self, kmh):
        if self.nopeus + kmh < 0:
            self.nopeus = 0
        elif self.nopeus + kmh > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus += kmh

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus

class Kilpailu:
    def __init__(self, kisanimi, pituus, osallistujat):
        self.kisanimi=kisanimi
        self.pituus=pituus
        self.osallistujat=[]

    def tunti_kuluu(self,tuntimaara):
        self.tuntimaara=tuntimaara
        for n in range(self.tuntimaara):
            for a in self.osallistujat:
                self.osallistujat[a].kiihdyta(random.randint(-10, 15))
                self.osallistujat[a].kulje(1)



    def kilpailu_ohi(self):
        pass

# kommentoituna alkuperäinen autokilpailu ennen tehtävää 10
# autot = []

# for n in range(10):
#     autot.append(Auto(('ABC-' + f'{n + 1}'), (random.randint(100,200))))
#
# while True:
#
#     for n in autot:
#         n.kiihdyta(random.randint(-10, 15))
#
#     for n in autot:
#         n.kulje(1)
#
#     if any(n.matka >= 10000 for n in autot):
#         break
#
#
# autot.sort(key=lambda a: a.matka, reverse=True)
# for n in autot:
#     print(f'REK: {n.rekisteritunnus}| MATKA:{n.matka}| NOPEUS:{n.nopeus}| HUIPPUNOPEUS:{n.huippunopeus}')


romuralli= Kilpailu.__init__(testikisa, 23, 23, f'{for o in range: