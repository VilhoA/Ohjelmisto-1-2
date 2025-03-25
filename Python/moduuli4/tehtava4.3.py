lukema = float(input('syötä lukema: '))
max = lukema
min = lukema
while True:
    lukema = (input('syötä lukema: '))

    if lukema == '':
        break

    lukema = float(lukema)
    if lukema >= max:
        max = lukema
    if lukema <= min:
        min = lukema
print ('suurin lukemasi: '+ str(max))
print ('pienin lukemasi: ' + str(min))
