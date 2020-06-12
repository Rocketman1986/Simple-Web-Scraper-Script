from bs4 import BeautifulSoup
import requests


Source = requests.get('https://www.stevenlivingstone.dev').text

Soup = BeautifulSoup(Source, 'lxml')

#print(Soup.prettify())

test = Soup.find_all('h1')

print(test)