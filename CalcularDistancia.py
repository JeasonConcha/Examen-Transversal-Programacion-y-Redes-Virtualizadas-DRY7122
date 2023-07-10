import requests

def calcular_distancia(ciudad_origen, ciudad_destino, api_key):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": ciudad_origen,
        "destinations": ciudad_destino,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    distancia_texto = data['rows'][0]['elements'][0]['distance']['text']
    distancia_km = float(distancia_texto.split(" ")[0].replace(",", ""))

    return distancia_km

# Solicitar las ciudades de origen y destino en español
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

# Obtener la clave de API de Google Maps
api_key = input("Clave de API de Google Maps: ")

# Calcular distancia en kilómetros utilizando la API de Google Maps
distancia_km = calcular_distancia(ciudad_origen, ciudad_destino, api_key)

# Imprimir el resultado
print("Distancia:", round(distancia_km, 1), "kms")