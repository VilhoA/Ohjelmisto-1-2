print ('Suorakulmion piiri ja pinta-ala')

kanta= input ('suorakulmion kanta: ')
kanta_arvo= float(kanta)

korkeus= input ('suorakulmion korkeus: ')
korkeus_arvo= float(korkeus)

print ('suorakulmion piiri: ' + str((kanta_arvo*2)+(korkeus_arvo*2)))
print ('suorakulmion ala: ' + str(kanta_arvo*korkeus_arvo))
