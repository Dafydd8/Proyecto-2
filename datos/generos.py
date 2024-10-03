from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import csv


def get_rta_1(driver):
    class_names = ["FozYP", "FLP8od", "IZ6rdc"]
    estilos = []
    for class_name in class_names:
        try:
            estilos = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
            break
        except:
            continue
    rv = []
    for estilo in estilos:
        rv.append(estilo.text)
    return rv
        
def buscar(driver, busqueda):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(busqueda)
    search_box.send_keys(Keys.ENTER)

f = open('spotify.csv', 'r', encoding='utf-8',)
albums = []
anios = []
streamss = []
for linea in csv.DictReader(f, delimiter=';'):
    album = linea['Album']
    anio = linea['Año']
    streams = linea['Streams']
    albums.append(album)
    anios.append(anio)
    streamss.append(streams)


chromedriverpath = './chromedriver'
try:
	driver = webdriver.Chrome()
except:
	driver = webdriver.Chrome(chromedriverpath)

f_out = open('generos.csv', 'w', encoding='utf-8')
f_out.write('Año;Album;Streams;Generos\n')

for i, album in enumerate(albums):
    print(album, "es:")
    busqueda = album + ' genre'
    buscar(driver, busqueda)
    rta = get_rta_1(driver)
    print(str(rta))
    f_out.write(f'{anios[i]};{album};{streamss[i]};{str(rta)}\n')

# Cerrar el navegador
driver.quit()

