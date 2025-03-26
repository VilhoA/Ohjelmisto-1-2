class Julkaisu:
    def __init__(self, nimi):
        self.nimi=nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja=kirjoittaja
        self.sivumaara=sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print (f'Nimi: {self.nimi} Kirjoittaja: {self.kirjoittaja} Sivumaara: {self.sivumaara}')

class Lehti(Julkaisu):
    def __init__(self,nimi, paatoimittaja):
        self.paatoimittaja=paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print (f'Nimi: {self.nimi} Paatoimittaja: {self.paatoimittaja}')

hytti= Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
aku= Lehti('Aku Ankka', 'Aki Hyyppä')

aku.tulosta_tiedot()
hytti.tulosta_tiedot()