
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

icao1= input("syötä ICAO #1: ")
icao2= input("syötä ICAO #2: ")
sql = f'select latitude_deg, longitude_deg from airport where ident = "{icao1}" or ident = "{icao2}";'



kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

cord1= tulos[0]
cord2= tulos[1]

from geopy import distance
kilometrit = (distance.distance(cord1, cord2).km)

print (f"Kenttien etäisyys kilometreissä: {kilometrit}")