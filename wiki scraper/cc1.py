import csv
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("Applications/Google Chrome.app")

url = 'https://www.myntra.com/shoes'

driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'lxml')

for shoes in soup.find_all('shoes'):

    name = shoes.find('meta', name="description")
    category = shoes.find('meta', )
    user_rating = shoes.find('')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow('name', 'category', 'user_rating')