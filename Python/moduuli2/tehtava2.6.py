# Tehtävänanto:
#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

#ensimmäinen koodi

koodi1=''
koodi1 += str (random.randint(0,9))
koodi1 += str (random.randint(0,9))
koodi1 += str (random.randint(0,9))

print('3 numeroinen arvottu koodi: ' + (koodi1)+('\n'))


#toinen koodi

koodi2=''
koodi2 += str (random.randint(1,6))
koodi2 += str (random.randint(1,6))
koodi2 += str (random.randint(1,6))
koodi2 += str (random.randint(1,6))

print('4 numeroinen arvottu koodi: ' + (koodi2))

