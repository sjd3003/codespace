import requests

URL = "C:/Users/sh/Documents/VeriFone/SRNTemp/rad6BB33.tmp_PLU.html"
page = requests.get(URL)

print(page.text)