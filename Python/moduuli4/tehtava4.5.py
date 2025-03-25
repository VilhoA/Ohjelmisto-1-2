yritykset = 5

while yritykset>0:

    käyttäjätunnus= input ('käyttäjätunnus: ')
    salasana= input ('salasana: ')

    if käyttäjätunnus == 'python' and salasana == 'rules':
        print ('Tervetuloa')
        break

    yritykset -= 1
if yritykset == 0:
    print('PÄÄSY EVÄTTY')
