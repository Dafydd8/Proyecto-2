import csv

f = open("albums.csv", "r", encoding="utf-8")

m = 10000000000000000
for line in csv.DictReader(f, delimiter=";"):
    n = int(line["Streams"])    
    if n < m:
        m = n

print(m)
