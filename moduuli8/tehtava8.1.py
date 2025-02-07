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
ICAO = input("syötä ICAO: ")

sql = f"SELECT name, municipality FROM airport where ident ='{ICAO}'"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
print (f'Nimi: {tulos[0][0]}')
print (f'Sijaintikunta: {tulos[0][1]}')