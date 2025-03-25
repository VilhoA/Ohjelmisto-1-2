import mysql.connector

yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database='flight_game',
    user= 'ville',
    password= 'villedb',
    autocommit=True,
    collation= 'utf8mb3_unicode_ci'
)

def haku(maakoodi, tyyppi):
    sql = f"SELECT type FROM airport  where iso_country = '{maakoodi}' and type = '{tyyppi}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    numero = 0
    for n in tulos:
        numero += 1
    return numero

useri= input("syötä maakoodi: ")
#
# sql = f"select distinct type from airport"
# kursori = yhteys.cursor()
# kursori.execute(sql)
# tulos = kursori.fetchall()
# print(tulos)
#
# for n in tulos:


#heliport
print (f'Heliport: {haku(useri, "heliport")}')
#small_airport
print (f'Small airport: {haku(useri, "small_airport")}')
#closed
print (f'Closed: {haku(useri, "closed")}')
#seaplane_base
print (f'Seaplane base: {haku(useri, "seaplane_base")}')
#balloonport
print (f'Balloonport: {haku(useri, "balloonport")}')
#medium_airport
print (f'Medium airport: {haku(useri, "medium_airport")}')
#large_airport
print (f'Large airport: {haku(useri, "large_airport")}')


