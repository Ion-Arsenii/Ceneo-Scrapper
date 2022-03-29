import requests
from bs4 import BeautifulSoup
url = "https://www.ceneo.pl/45863470#tab-reviews"
response = requests.get(url)


pag3_dom = BeautifulSoup(response.text, "htmll.parser")


opiniaons = page_dom.select("div.js_product-review")
opinion = opinions.pop()
print(opinion.pretiffy())