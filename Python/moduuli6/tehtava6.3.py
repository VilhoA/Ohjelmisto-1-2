
litrat= 0

def konversio(muunto):
    return muunto * 3.785

while True:
    galloonat = float(input('syötä galloonat: '))
    if galloonat < 0:
        break
    if galloonat >= 0:
        litrat = konversio (galloonat)
        print (f'galloonat litroina: {litrat}')


