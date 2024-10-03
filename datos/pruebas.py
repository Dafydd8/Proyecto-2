a = ['a', 'b', 'c', 'd']
print((str(a)))
b = str(a)
print(b.split("', '"))
f = open('out.csv', 'w', encoding='utf-8')
f.write(str(a))