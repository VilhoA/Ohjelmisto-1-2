vuosi= int(input('kerro vuosiluku: '))

#if (vuosi % 100 == 0 and vuosi % 400 == 0):
#    print ('vuosi ' + str(vuosi) + ' on karkausvuosi')
#elif (vuosi % 4 == 0):
#        print ('vuosi '+ str(vuosi) + ' on karkausvuosi')

#else:
#   print ('vuosi ' + str (vuosi) + ' ei ole karkausvuosi')

if (vuosi % 4 == 0 and vuosi % 100 != 0):
    print ('vuosi ' + str(vuosi) + ' on karkausvuosi')

elif (vuosi % 400 == 0):
    print ('vuosi ' + str(vuosi) + ' on karkausvuosi')

else:
    print ('vuosi ' + str(vuosi) + ' ei ole karkausvuosi')