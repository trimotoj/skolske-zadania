krajiny=[]
pocet=[]
meno=[]
vysledok=[]

with open('zadanie23/skok_do_dialky','r') as file:
    line=file.readline().split()
    krajiny.append(line[1])
    pocet.append(1)
    meno.append(line[0])
    body=0
    for i in line[2:]:
            if int(i) > body:
                body = int(i)
    vysledok.append(body)
    for line in file:
        body=0
        line=line.split()
        meno.append(line[0])
        for i in line[2:]:
            if int(i) > body:
                body = int(i)
        vysledok.append(body)
        for i in range(len(krajiny)):
            if line[1] == krajiny[i]:
                pocet[i] += 1
        if line[1] not in krajiny:
            krajiny.append(line[1])
            pocet.append(1)

    for i in range(len(krajiny)):
        print(str(pocet[i])+'x '+krajiny[i])

    vitazi=''   
    for i in range(len(vysledok)):
        if vysledok[i] == body:
            vitazi += meno[i]+' '
    print('Víťazi: '+vitazi)