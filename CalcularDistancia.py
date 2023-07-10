import requests

def calcular_distancia(ciudad_origen, ciudad_destino):
    url = f"https://www.distance24.org/route.json?stops={ciudad_origen}|{ciudad_destino}"
    response = requests.get(url)
    data = response.json()
    distancia_km = data['distance']

    return distancia_km

def calcular_duracion(distancia_km, velocidad_promedio):
    tiempo_horas = distancia_km / velocidad_promedio
    tiempo_minutos = tiempo_horas * 60
    tiempo_segundos = tiempo_minutos * 60

    return tiempo_horas, tiempo_minutos, tiempo_segundos

def calcular_combustible(distancia_km, rendimiento_combustible):
    litros_combustible = distancia_km / rendimiento_combustible

    return litros_combustible

# Solicitar las ciudades de origen y destino
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

# Calcular distancia
distancia_km = calcular_distancia(ciudad_origen, ciudad_destino)

# Calcular duración del viaje
velocidad_promedio = 80  # km/h (ejemplo, puedes ajustarlo según tus necesidades)
tiempo_horas, tiempo_minutos, tiempo_segundos = calcular_duracion(distancia_km, velocidad_promedio)

# Calcular combustible requerido
rendimiento_combustible = 10  # km/l (ejemplo, puedes ajustarlo según tus necesidades)
litros_combustible = calcular_combustible(distancia_km, rendimiento_combustible)

# Imprimir los resultados
print("Distancia:", round(distancia_km, 1), "kms")
print("Duración del viaje:", round(tiempo_horas, 1), "horas,", round(tiempo_minutos, 1), "minutos,", round(tiempo_segundos, 1), "segundos")
print("Combustible requerido:", round(litros_combustible, 1), "litros")
print("S")
print("Narrativa del viaje:")
print("Viaje desde", ciudad_origen, "hasta", ciudad_destino)

# Agregar el código para subir el script al repositorio de GitHub con un commit a elección.
# Utiliza los comandos de Git para agregar y subir el archivo al repositorio.
# Por ejemplo:
# git add script.py
# git commit -m "Agregado script de cálculo de distancia y duración de viaje"
# git push origin main