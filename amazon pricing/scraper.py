import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?crid=2MHUP2JQ09IQV&keywords=sony+a7&qid=1668323570&qu=eyJxc2MiOiI0LjYxIiwicXNhIjoiNC4yNiIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=sony+a7%2Caps%2C366&sr=8-1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


title = soup.find(id="productTitle").get_text()
price = soup.find(id=)
print(title.strip())
