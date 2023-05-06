zastavky=[]
capacity=0
preplneni=[]
pocet_ludi=()
with open('zadanie29/vstup',encoding='utf-8') as file:
    max_capacity=int(file.readline())
    for line in file:
        line = line.split()
        zastavky.append(' '.join(line[2:]))
        capacity+=int(line[0])-(int(line[1]))
        if capacity > max_capacity:
            preplneni.append(' '.join(line[2:]))
        pocet_ludi+=capacity,

print('pocet zastavok:',len(zastavky))
print('nazvy zastavok: '+', '.join(zastavky))
print('Zasavky po nastupeni preplneni: '+', '.join(preplneni))
print('Najvyssi pocet ludi v autobuse:',max(pocet_ludi))