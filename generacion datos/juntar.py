# ARCHIVO AUXILIAR

import csv

f_out = open('spotify_juntado.csv', 'w', encoding='utf-8')
f_out.write('Año;Album;Streams\n')

for i in range(21):
    if i  % 2 == 0:
        print("hola")
        f = open(f'{2003+i}.csv', 'r', encoding='utf-8')
    else:
        f = open(f'Most streamed albums on Spotify - {2003+i}.csv', 'r', encoding='utf-8')
    for linea in csv.DictReader(f):
        album = linea['Album']
        streams = linea['Streams'].replace(',', '')
        año = 2003+i
        f_out.write(f'{año};{album};{streams}\n')