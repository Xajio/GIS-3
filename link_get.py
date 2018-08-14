import re
import requests
import bs4

url = "https://observatorio.osinfor.gob.pe/Observatorio/Home/listaRoja"

u2 = 'https://sisfor.osinfor.gob.pe/visor/geoObsROJO/'

r = requests.get(url).text

soup = bs4.BeautifulSoup(r)

number_regex = re.compile("\([0-9]+,[0-9]+\)")

numbers = []
links = []

for img in soup.findAll('img', style="cursor:pointer;"):
        print(re.findall(img, number_regex))
        numbers_splitted = img.split(",")
        links.append(u2 +numbers_splitted[0] +"|" +numbers_splitted[1])



print(r)