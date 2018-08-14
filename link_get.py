import re
import requests
import bs4

url = "https://observatorio.osinfor.gob.pe/Observatorio/Home/listaRoja"

u2 = 'https://sisfor.osinfor.gob.pe/visor/geoObsROJO/'
"""

"""
r = requests.get(url).text

soup = bs4.BeautifulSoup(r, "lxml")

number_regex = re.compile("[0-9]+,[0-9]+")

links = []

for img in soup.findAll('img', style="cursor:pointer;"):
        str_numbers = re.findall(number_regex, img.attrs["onclick"])[0]
        numbers_splitted = str_numbers.split(",")
        links.append(u2 + numbers_splitted[0] +"|" +numbers_splitted[1])



print(links)