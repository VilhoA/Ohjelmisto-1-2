lista = [2,3,4,7,6]

def karsi(lista):
    parillinen = []
    for n in lista:
        if n % 2 == 0:
            parillinen.append (n)
    return parillinen


print (lista)
print (karsi(lista))