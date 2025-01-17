print ('Massanmuuntomasiina!')

#käyttäjän input
leiviska= float(input('syötä leiviskät: '))
naula= float(input('syötä naulat: '))
luoti= float(input('syötä luodit: '))

kokonaisgrammat= float(leiviska * 8512 + (naula * 425.6 + (luoti * 13.3)))
kokonaiskilot= int(kokonaisgrammat / 1000)
grammat= float (kokonaisgrammat - int( kokonaiskilot * 1000 ))

print ('Massat nykyarvoihin muutettuna!')
print ('kilot: ' + str(kokonaiskilot))
print (('grammat: ') + f'{grammat:.2f}')
#perusarvot
#luoti on 13.3 g
#naula on 32x13.3= 425.6 g
#leisivkä on 20x425.6= 8512 g
