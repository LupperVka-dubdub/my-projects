import requests
from bs4 import BeautifulSoup

url = input("Enter Link:")

if "https" or "http" in url:
    data = requests.get(url)
else:
    data = requests.get("https://" + url)

soup = BeautifulSoup(data.text,"html.parser")
links = []
for link in soup.find_all("a"):
    links.append(f"https://books.toscrape.com/" + link.get("href"))

with open("malinks.text","w") as saved:
    for lk in links[:10]:
        print(lk, file=saved)