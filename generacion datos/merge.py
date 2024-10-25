import csv
f = open('albums_generos_reducidos.csv', 'r', encoding='utf-8')
f_out = open('albums.csv', 'w', encoding='utf-8')
f_out.write('Año;Album;Streams;Generos\n')
for linea in csv.DictReader(f, delimiter=';'):
    anio = linea['Año']
    album = linea['Album']
    generos = linea['Generos_Reducidos']
    streams = linea['Streams']
    f_out.write(f'{anio};{album};{streams};{generos}\n')

f.close()
f_out.close()
