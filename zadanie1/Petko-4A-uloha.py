zoznam_cisel=[]
while True:
    pomocna_premenna = 0
    cislo=int(input('Zadaj integer: '))
    for i in range(len(zoznam_cisel)):
        if zoznam_cisel[i][0] == cislo:
            pomocna_premenna = 1
            zoznam_cisel[i][1] += 1

    if pomocna_premenna == 0:        
        zoznam_cisel.append([cislo,1])

    for i in range(len(zoznam_cisel)-1,0,-1):  
        for j in range(i):  
             if zoznam_cisel[j][0] > zoznam_cisel[j+1][0]:
                zoznam_cisel[j] , zoznam_cisel[j+1] = zoznam_cisel[j+1] , zoznam_cisel[j]            
    
    subor=open('status','w')
    subor.write('Zadane cisla: ')
    for i in range(len(zoznam_cisel)):
        subor.write(str(zoznam_cisel[i][0])+'('+str(zoznam_cisel[i][1])+'x), ')
    if len(zoznam_cisel) > 2:
        for i in range(len(zoznam_cisel)-1,0,-1):  
            for j in range(i):
                if zoznam_cisel[j][1] > zoznam_cisel[j+1][1]:
                    zoznam_cisel[j] , zoznam_cisel[j+1] = zoznam_cisel[j+1] , zoznam_cisel[j]
        subor.write('\n')
        subor.write('Tri cisla s najvacsim poctom vyskytov: ')
        for i in range(1,4):
            subor.write(str(zoznam_cisel[-i][0])+'('+str(zoznam_cisel[-i][1])+'x), ')

    else:
        subor.write('\n')
        subor.write('Neboli zadane 3 rozne cisla')

    print('data boli ulozene do suboru :)')
    subor.close()    