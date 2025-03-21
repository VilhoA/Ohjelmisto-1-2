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


autot = []

for n in range(10):
    autot.append(Auto(('ABC-' + f'{n + 1}'), (random.randint(100,200))))

while True:

    for n in autot:
        n.kiihdyta(random.randint(-10, 15))

    for n in autot:
        n.kulje(1)

    if any(n.matka >= 10000 for n in autot):
        break


autot.sort(key=lambda a: a.matka, reverse=True)
for n in autot:
    print(f'REK: {n.rekisteritunnus}| MATKA:{n.matka}| NOPEUS:{n.nopeus}| HUIPPUNOPEUS:{n.huippunopeus}')
