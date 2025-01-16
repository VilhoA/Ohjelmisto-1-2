print ('massanmuuntomasiina')

#käyttäjän input
leiviska= float(input('syötä leiviskät: '))
naula= float(input('syötä naulat: '))
luoti= float(input('syötä luodit: '))

kokonaisgrammat= float(leiviska * 8512 + (naula * 425.6 + (luoti * 13.3)))
kokonaiskilot= int(kokonaisgrammat / 1000)
desimaali= (float(kokonaisgrammat) - int(kokonaisgrammat))

print ('kilot: ' + str(kokonaiskilot))
print(('kokonaisgrammat: ') + f'{desimaali:.3f}')
#perusarvot
#luoti on 13.3 g
#naula on 32x13.3= 425.6 g
#leisivkä on 20x425.6= 8512 g
