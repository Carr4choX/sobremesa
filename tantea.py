import requests

OBJETIVO = "http://reservas.carballesa.test"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; CarrachoBot/0.1)"}

with open("rutas.txt") as f:
    RUTAS = [linea.strip() for linea in f if linea.strip()]

for ruta in RUTAS:
    r = requests.get(OBJETIVO + ruta, headers=HEADERS, timeout=3)
    print(ruta, r.status_code)
