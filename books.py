import requests
from bs4 import BeautifulSoup

import csv

response = requests.get('https://books.toscrape.com/')

# print(response.status_code)

soup = BeautifulSoup(response.content,'html.parser')
# print(soup)

books = soup.find_all('article', class_='product_pod')
data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p',class_= 'price_color').text
    availability = book.find('p',class_="instock availability").text.strip()
    data.append([title,price,availability])

# print(data)

with open('bookstore.csv','w')as file:
    writer=csv.writer(file)
    writer.writerow(["Title","Price","Availability"])
    writer.writerows(data)
    