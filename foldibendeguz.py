jegy=open('/home/foldibendeguz/jegy.txt','r')
lista = []
c = []
d=0
for sor in jegy:
    lista.append(sor[:-1])
for a in lista:
    if a != "":
        c.append(a)
        d=d+1
e = map(int, c)
print(sum(e)/d)
