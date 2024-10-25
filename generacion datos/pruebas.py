import csv
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import csv

def get_image(driver, link):
    driver.get(link)
    img_elem = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'mMx2LUixlnN_Fu45JpFB')))
    #img_elem = img_div[0].find_element_by_tag_name('img')
    rta = img_elem[0].get_attribute('src')
    return rta

f = open('albums_copy.csv', 'r', encoding='utf-8',)

links = []
for linea in csv.DictReader(f):
    link = linea['Link']
    links.append(link)

f.close()

f = open('albums_copy.csv', 'r', encoding='utf-8',)

lineas = []
for linea in f:
    lineas.append(linea.strip())
encabezado = lineas.pop(0)
    
chromedriverpath = './chromedriver'
try:
	driver = webdriver.Chrome()
except:
	driver = webdriver.Chrome(chromedriverpath)

f_out = open('links_album.csv', 'w', encoding='utf-8')
f_out.write(encabezado + ',LinkImg\n')

for i, link in enumerate(links):
    rta = get_image(driver, link)
    f_out.write( lineas[i] + ',' + rta + '\n')

# Cerrar el navegador
driver.quit()

