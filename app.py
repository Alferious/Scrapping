import requests
from bs4 import BeautifulSoup

response = requests.get('https://zinduaschool.com/')

# print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

links = soup.find_all('a')

for links in links:
    href = links.get('href')




