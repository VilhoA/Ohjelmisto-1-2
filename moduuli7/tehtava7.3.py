# Lentoasemia
lentokentat= {"EFRN":"Rovaniemi airport",
              "EFHK":"Helsinki-Vantaa Airport",
              "EFIV":"Ivalo Airport",
              "EFKI":"Kajaani Airport"}

while True:
    useri= input("Haluatko syöttää uuden lentokentän, hakea jo syötetyn vai lopettaa? Komennot: 'uusi', 'hae', 'lopeta' ")
    if useri =="lopeta":
        break
    elif useri == "hae":
        ICAO= (input("syötä kentän ICAO: ").upper())
        if ICAO in lentokentat:
            print (f"Koodia vastaavan kentän nimi: {lentokentat[ICAO]}")

    elif useri == "uusi":
        uusinimi= input("syötä kentän nimi: ")
        uusiICAO= input("syötä kentän ICAO: ").upper()

        lentokentat[uusiICAO] = uusinimi



