sukupuoli= input('syötä sukupuoli: ').lower()

harvo= float (input('syötä hemoglobiiniarvosi (g/l): '))

if sukupuoli== 'mies':
    if float (harvo) < 134:
        print ('hemoglobiinisi on alhainen')

    if float (harvo) > 195:
        print ('hemoglobiinisi on korkea')

    if float (harvo) >= 134 and (harvo) <= 195:
        print ('hemoglobiinisi on normaali')

elif sukupuoli=='nainen':

    if float (harvo) < 117:
        print ('hemoglobiinisi on alhainen')

    if float (harvo) > 175:
        print ('hemoglobiinisi on korkea')

    if float (harvo) >= 117 and (harvo) <= 175:
        print ('hemoglobiinisi on normaali')

else:
    print ('virheellinen sukupuoli')



