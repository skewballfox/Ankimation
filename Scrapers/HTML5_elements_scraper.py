import requests
from bs4 import BeautifulSoup

url='https://www.w3schools.com/tags/ref_byfunc.asp'

request = requests.get(url)

soup = BeautifulSoup(request.content, 'html.parser')

print (soup)