from random import *
pismena=[]
nove_slovo=''
subor2=open('poprehadzovany_text.txt','w')
with open('zadanie3/textvstup.txt','r') as subor:
    for riadok in subor:
        riadok=riadok.split()
        for slovo in riadok:
            for pismeno in slovo[1:-1]:
                pismena.append(pismeno)
            for i in range(len(pismena)):
                vymena = randrange(len(pismena))
                pismena[i] , pismena[vymena] = pismena[vymena] , pismena[i]
            for j in pismena:
                nove_slovo+=j
            subor2.write(slovo[0]+nove_slovo+slovo[-1]+' ')
            pismena=[]
            nove_slovo=''
        subor2.write('\n')
subor2.close()        

            


