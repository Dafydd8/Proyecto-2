import csv

f=open("albums_copy.csv", "r")

max = 0
for linea in csv.DictReader(f):
    if int(linea["Streams"]) > max:
        max = int(linea["Streams"])
        album = linea["Album"]
print(album, max)