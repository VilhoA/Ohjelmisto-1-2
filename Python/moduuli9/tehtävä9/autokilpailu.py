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
        self.osallistujat= osallistujat

    def tunti_kuluu(self):
        for a in self.osallistujat:
            a.kiihdyta(random.randint(-10, 15))
            a.kulje(1)

    def tulosta_tilanne(self,):
        print('----------------------------------')
        for n in self.osallistujat:
            print(f'Matka: {n.matka:5}|, Nopeus: {n.nopeus:5}|, Huippunopeus: {n.huippunopeus:5}|, Rekisteritunnus: {n.rekisteritunnus:8}|')


    def kilpailu_ohi(self):
        for n in osallistujat:
            if n.matka > self.pituus:
                return True
        return False

osallistujat= []
for n in range(10):
    osallistujat.append(Auto(('ABC-' + f'{n + 1}'), (random.randint(100,200))))


romuralli = Kilpailu('Suuri romuralli', 8000, osallistujat)


while not romuralli.kilpailu_ohi():
    tunnit = 0
    romuralli.tunti_kuluu()
    if tunnit % 10 == 0:
        romuralli.tulosta_tilanne()
print()
print()
print('Lopputulos')
print()
romuralli.tulosta_tilanne()

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


