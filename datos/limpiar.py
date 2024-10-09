import csv

f = open("nuevos albums.csv", "r", encoding="utf-8")
f_out = open("albums_2.csv", "w", encoding="utf-8") 
f_out.write("Año,Album,Streams,Generos,Valoracion\n")

for linea in f:
    s = linea.replace("\"", "")
    if s[-1] == ',':
        s = s[:-1]
    f_out.write(s)

f.close()
f_out.close()