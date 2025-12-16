import requests
from bs4 import BeautifulSoup

url = "https://store.steampowered.com/search/?filter=topsellers"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
print("Status:", response.status_code)

if response.status_code != 200:
    print(" No se pudo acceder")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

juegos = []

for item in soup.select("a.search_result_row"):
    nombre_tag = item.select_one("span.title")
    link = item.get("href")

    if nombre_tag and link:
        nombre = nombre_tag.text.strip()
        juegos.append({
            "nombre": nombre,
            "link": link
        })

with open("juegos_steam.txt", "w", encoding="utf-8") as f:
    for j in juegos:
        f.write(f"{j['nombre']} | {j['link']}\n")

print(f" Juegos guardados: {len(juegos)}")
for j in juegos:
    print(f" - {j['nombre']} | {j['link']}")
