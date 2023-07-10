from geopy.geocoders import Nominatim
from geopy import distance

def obtener_distancia(ciudad_origen, ciudad_destino):
    geolocator = Nominatim(user_agent="app")
    location_origen = geolocator.geocode(ciudad_origen)
    location_destino = geolocator.geocode(ciudad_destino)
    coords_origen = (location_origen.latitude, location_origen.longitude)
    coords_destino = (location_destino.latitude, location_destino.longitude)
    return distance.distance(coords_origen, coords_destino).km

ciudad_origen = input("Ciudad De Origen: ")
ciudad_destino = input("Ciudad De Destino: ")

distancia_km = obtener_distancia(ciudad_origen, ciudad_destino)

tiempo_horas = distancia_km / 100
tiempo_minutos = tiempo_horas * 60
tiempo_segundos = tiempo_minutos * 60

combustible_litros = distancia_km * 0.15

print("Duracion del viaje: {} horas, {} minutos, {} segundos".format(int(tiempo_horas), int(tiempo_minutos), int(tiempo_segundos)))
print("Combustible requerido: {} litros".format(round(combustible_litros, 1)))

print("¡Estás a punto de viajar desde {} a {}!".format(ciudad_origen, ciudad_destino))
print("El viaje tiene una distancia de {} km y tomará aproximadamente {} horas.".format(round(distancia_km, 1), int(tiempo_horas)))