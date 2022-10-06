from random import *
ziaci=int(input("Zadaj pocet studentov: "))
otazky=int(input("Zadaj pocet otazok: "))
while ziaci > otazky:
    if ziaci > otazky:
        print('bol zadany maly pocet otazok')
        ziaci=int(input("Zadaj pocet studentov: "))
        otazky=int(input("Zadaj pocet otazok: "))

zoznam_studentov=[]
poradie_studentov=[]
for i in range(ziaci):
    zoznam_studentov.append(i+1)

while len(zoznam_studentov) != len(poradie_studentov):
    ziak=randint(1,ziaci)
    if ziak in poradie_studentov:
        continue 
    else:
        poradie_studentov.append(ziak)

zoznam_otazok=[]
poradie_otazok=[]
poradie_otazok.append(randint(1,otazky))
for i in range(otazky):
    zoznam_otazok.append(i+1) 

i=0
while len(zoznam_studentov) != len(poradie_otazok):
    otazka=randint(1,otazky)
    if otazka in poradie_otazok:
        continue
    else:
        if otazka % 2 != poradie_otazok[i] % 2: 
            poradie_otazok.append(otazka)  
            i+=1

for i in range(len(poradie_studentov)):
    print(str(i+1)+'. student: '+str(poradie_studentov[i])+', otazka: '+str(poradie_otazok[i]))


