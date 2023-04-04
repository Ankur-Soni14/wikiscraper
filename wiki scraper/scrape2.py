import random
import requests
from bs4 import BeautifulSoup


def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

match = soup.find()