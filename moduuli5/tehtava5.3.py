
luku = int(input('syötä kokonaisluku: '))

if luku <2:
    print ('luku ei ole alkuluku')

else:

    alkuluku = 1

    for x in range(2, luku):
        if luku % x == 0:
            alkuluku = 0
            break

if alkuluku == 1:
    print ('luku ', (luku), ' on alkuluku')

else:
    print ('luku ', (luku), ' ei ole alkuluku' )
