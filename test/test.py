from bs4 import BeautifulSoup
import requests
url = 'https://Users/sh/Documents/VeriFone/SRNTemp/radBA089.tmp_PLU.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print (soup)