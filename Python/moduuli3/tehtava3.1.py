kuhamitta= float(input('syötä kuhan mitta senttimetreissä: '))
if kuhamitta <37:
    print (f'kuhasi on {37-kuhamitta: .1f} senttimetriä alimittainen')
    print ('laske se takaisin järveen!')
else:
    print ('voit pitää kuhan!')

#tehtävänannossa ei mainittu desimaaleista joten päätin näyttää vajavaisuuden yhdellä desimaalilla