import requests

OBJETIVO = "http://reservas.carballesa.test"
RUTAS = ["/", "/admin", "/backup"]
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; CarrachoBot/0.1)"}

for ruta in RUTAS:
    r = requests.get(OBJETIVO + ruta, headers=HEADERS, timeout=5)
    print(ruta, r.status_code)
