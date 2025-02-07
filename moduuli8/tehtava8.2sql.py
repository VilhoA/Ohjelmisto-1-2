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

maakoodi = input('syötä maakoodi: ')

sql = f"select type, count(*) from airport where iso_country = '{maakoodi}' group by type"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

for n in tulos:
    print (f"Kentän tyyppi: {n[0]}                     Määrä: {n[1]}")