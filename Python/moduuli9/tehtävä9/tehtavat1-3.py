
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

lada = Auto('ABC-123', 142)

print (lada.nopeus, lada.matka, lada.huippunopeus, lada.rekisteritunnus)
print('\n')

lada.kiihdyta(30)
lada.kiihdyta(70)
lada.kiihdyta(50)
print (lada.nopeus)
lada.kiihdyta(-42)
print (lada.nopeus)
lada.kulje(2)
print(lada.matka)


