from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(ciudad)
    if location:
        return location.latitude, location.longitude
    else:
        return None

def calcular_distancia(ciudad_origen, ciudad_destino):
    coordenadas_origen = obtener_coordenadas(ciudad_origen)
    coordenadas_destino = obtener_coordenadas(ciudad_destino)

    if coordenadas_origen and coordenadas_destino:
        distancia = geodesic(coordenadas_origen, coordenadas_destino).kilometers
        return distancia
    else:
        return None

distancia_km = calcular_distancia(ciudad_origen, ciudad_destino)
if distancia_km:
    print("La distancia entre {ciudad_origen} y {ciudad_destino} es de {distancia_km:.1f} km.")
else:
    print("No se pudo calcular la distancia.")