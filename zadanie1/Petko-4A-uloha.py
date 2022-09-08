zoznam_cisel=[]
pomocna_premenna = 0
while True:
    print('Ak chces program ukoncit, zadaj do vstupu string')
    cislo=input('Zadaj integer: ')
    if cislo.isdigit():
        for i in range(len(zoznam_cisel)):
            if zoznam_cisel[i][0] == cislo:
                pomocna_premenna = 1
                zoznam_cisel[i]=list(zoznam_cisel[i])
                zoznam_cisel[i][1]+=1
                zoznam_cisel[i]=tuple(zoznam_cisel[i])

        if pomocna_premenna == 0:        
            zoznam_cisel.append((cislo,1))
        pomocna_premenna = 0

        for i in range(0,len(zoznam_cisel)-1):  
            for j in range(len(zoznam_cisel)-1):  
                if zoznam_cisel[j][0]>zoznam_cisel[j+1][0]:
                    zoznam_cisel[j] = list(zoznam_cisel[j])
                    zoznam_cisel[j+1] = list(zoznam_cisel[j+1])
                    temp = zoznam_cisel[j][0]  
                    zoznam_cisel[j][0] = zoznam_cisel[j+1][0]  
                    zoznam_cisel[j+1][0] = temp
                    zoznam_cisel[j] = tuple(zoznam_cisel[j])
                    zoznam_cisel[j+1] = tuple(zoznam_cisel[j+1]) 
    else:
        print('data boli ulozene v subore')
        subor=open('data','w')
        for i in range(len(zoznam_cisel)):
            subor.write(str(('cislo',zoznam_cisel[i][0],'bolo zadane',zoznam_cisel[i][1],'krat')))
        subor.write('\n')
        subor.write(str(('tri najvacsie cisla ',zoznam_cisel[-3][0],',',zoznam_cisel[-2][0],',',zoznam_cisel[-1][0],'s poctom vyskytov: ',zoznam_cisel[-3][1],',',zoznam_cisel[-2][1],',',zoznam_cisel[-1][1])))
        break
    