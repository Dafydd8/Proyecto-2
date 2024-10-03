a = ['a', 'b', 'c', 'd']
print((str(a)))
b = str(a)
print(b.split("', '"))
f = open('out.csv', 'w', encoding='utf-8')
f.write(str(a))

a = 5000000000
def poner_comas(n):
    s = str(n)
    rv = ''
    coma = 0
    for i in range(len(s)):
        if coma == 2:
            rv += s[-i-1]
            rv += ','
            coma = 0
        else:
            rv += s[-i-1]
            coma += 1
    return rv[::-1]
b = poner_comas(a)    
print(b)