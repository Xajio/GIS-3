url2 = 'https://sisfor.osinfor.gob.pe/visor/geoObsROJO/20130002429|1'

import requests

r = requests.get(url2).text


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(url2)

element = driver.find_element_by_id("btnterminoUso")
element.send_keys("", Keys.ARROW_DOWN)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
