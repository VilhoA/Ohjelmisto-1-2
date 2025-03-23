class Hissi:
    def __init__(self, alinkerros, ylinkerros,):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.nykykerros = 0

    def kerros_ylös(self):
        self.nykykerros += 1

    def kerros_alas(self):
        self.nykykerros -= 1

    def siirry_kerrokseen(self, kerros):
        while self.nykykerros != kerros:

            if self.nykykerros < kerros:
                self.kerros_ylös()

            if self.nykykerros > kerros:
                self.kerros_alas()

class Talo:
    def __init__(self,alin,ylin,lkm):
        self.alin=alin
        self.ylin=ylin
        self.hissit=[]
        self.lkm = lkm
        for n in range(self.lkm):
            muuttuja=Hissi(alin,ylin)
            self.hissit.append(muuttuja)

    def aja_hissia(self,hnmr,kerros):
        self.hissit[hnmr].siirry_kerrokseen(kerros)

    def tulipalo(self):
        for n in range(self.lkm):
            self.aja_hissia(n,self.alin)



hissi1 = Hissi(1,10)

hissi1.siirry_kerrokseen(5)
print(hissi1.nykykerros)

hissi1.siirry_kerrokseen(hissi1.alinkerros)
print(hissi1.nykykerros)


talo1 = Talo(0,15,3)

talo1.aja_hissia(1,5)
talo1.aja_hissia(0,0)
talo1.aja_hissia(2,15)

for n in talo1.hissit:
    print(n.nykykerros)

talo1.tulipalo()

for n in talo1.hissit:
    print(f'Palohälyn jälkeinen kerros: {n.nykykerros}')




