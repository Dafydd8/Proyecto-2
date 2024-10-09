import csv

f = open("albums.csv", "r", encoding="utf-8")
f_out = open("albums_copy.csv", "w", encoding="utf-8") 
f_out.write("Año,Album,Streams,Generos,Valoracion,aoty,soty\n")

ganadores_album = ['Speakerboxxx/The Love Below', '21', 'When We All Fall Asleep Where Do We Go?', 'Folklore', 'Harry\'s House', 'Midnights', '25', '1989']
ganadores_cancion = ['Back to Black', 'Viva La Vida Or Death And All His Friends', 'I Am...Sasha Fierce', 'Pure Heroine', 'Multiply (x)', '25', 'When We All Fall Asleep Where Do We Go?']

for linea in csv.DictReader(f):
    anio = linea['Año']
    album = linea['Album']
    artista = linea['Artista']
    streams = linea['Streams']
    genero = linea['Generos']
    valoracion = linea['Valoracion']
    s = f'{anio},{album},{artista},{streams},{genero},{valoracion}'
    if linea['Album'] in ganadores_album:
        s = s + ',1'
    else:
        s = s + ',0'
    if linea['Album'] in ganadores_cancion:
        s = s + ',1\n'
    else:
        s = s + ',0\n'
    f_out.write(s)
    

f.close()
f_out.close()