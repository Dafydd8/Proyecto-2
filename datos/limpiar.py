import csv

f = open("albums_2.csv", "r", encoding="utf-8")
f_out = open("albums.csv", "w", encoding="utf-8") 
f_out.write("Año,Album,Streams,Generos,Valoracion\n")

i = 0
cont = 0
for linea in f:
    if cont == 5:
        cont = 0
        i += 1
    linea = str(2003 + i)+','+linea
    f_out.write(linea)
    cont += 1

f.close()
f_out.close()