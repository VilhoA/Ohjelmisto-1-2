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

class Sahkoauto(Auto):
    def __init__(self, akkukapasiteetti, rekisteritunnus, huippunopeus):
        self.akkukapasiteetti=akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttis(Auto):
    def __init__(self, bensatankkikoko, rekisteritunnus, huippunopeus):
        self.bensatankkikoko=bensatankkikoko
        super().__init__(rekisteritunnus, huippunopeus)

nikko= Sahkoauto(52.5, 'ABC-15', 180)
polttisauto= Polttis(32.3, 'ACD-123', 165)

nikko.nopeus= 100
polttisauto.nopeus= 120

nikko.kulje(3)
polttisauto.kulje(3)

print(f'Polttomoottoriauton matka: {polttisauto.matka}')
print(f'Sahkoauton matka: {nikko.matka}')