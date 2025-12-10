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
    print("❌ No se pudo acceder")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

juegos = []

for span in soup.find_all("span", class_="title"):
    nombre = span.get_text(strip=True)
    if nombre:
        juegos.append(nombre)

with open("juegos_steam.txt", "w", encoding="utf-8") as f:
    for j in juegos:
        f.write(j + "\n")

print(f"✅ Juegos guardados: {len(juegos)}")
