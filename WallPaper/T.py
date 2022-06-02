import requests
from bs4 import BeautifulSoup

data = requests.get('https://wallhaven.cc/')
soup = BeautifulSoup(data.text, "lxml")
urls = [item.attrs["href"] for item in soup.select('#featured > div.pop-tags > span > a')]
print(urls)
