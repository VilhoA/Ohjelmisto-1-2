#Matematiikka 2 tehtävien 1 python osuus


#Esimerkki tehtävä
import numpy

a = 48
b = 171

print(f'Alfa kulma radiaaneina: {numpy.radians(a)}')
print(f'Beeta kulma radiaaneina: {numpy.radians(b)}')


#Muunnetaan radianit asteiksi
a = 2.493
b = 0.911

print(f'A radiaani asteina: {numpy.degrees(a)}')
print(f'B radiaani asteina: {numpy.degrees(b)}')


#Muunnetaan asteet radiaaneiksi

a = 137.7
b = 62.3

print(f'Alfa kulma radiaaneina: {numpy.radians(a)}')
print(f'Beeta kulma radiaaneina: {numpy.radians(b)}')


#Tehdään numpylla taulukko

taulukko = numpy.array([30,45,60,90,120,135,150,180,270,360])

for n in taulukko:
    print(numpy.radians(n))

print('\n')

#Ratkaistaan kolmion hypotenuusan pituus

a = (numpy.hypot(1.6, 2.3))

print(f'Kolmion hypotenuusan pituus on: {a} metriä')