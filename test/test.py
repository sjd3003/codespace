from bs4 import BeautifulSoup
import requests
url = 'file:///C:/Users/sh/Documents/VeriFone/SRNTemp/radBA089.tmp_PLU.html'
response = requests.get(url)
print (response.json())
