#kuukaudet = ('tammikuu', 'helmikuu', 'maaliskuu', 'huhtikuu', 'toukokuu', 'kesakuu', 'heinakuu', 'elokuu', 'syyskuu', 'lokakuu', 'marraskuu', 'joulukuu')
#print (kuukaudet)

def vuodenaika(input):
        if input in kevat:
            return ('kevat')
        if input in kesa:
            return ('kesa')
        if input in (syksy):
            return ('syksy')
        if input in (talvi):
            return ('talvi')


kevat = (3, 4, 5)
kesa = (6, 7, 8)
syksy = (9, 10, 11)
talvi = (12, 1, 2)

useri= int(input('syötä kuukauden numero saadaksesi vuodenajan: '))

print (vuodenaika(useri))


#toinen tapa
print("--------------------")
useri= int(input('syötä kuukauden numero saadaksesi vuodenajan: '))
while True:
    if useri >=3 and useri <=5:
        print ('kevät')
        break

    elif useri >=6 and useri <=8:
        print ('kesä')
        break

    elif useri >=9 and useri <=11:
        print ('syksy')
        break

    elif useri == 12 or 1 or 2:
        print ('talvi')
        break