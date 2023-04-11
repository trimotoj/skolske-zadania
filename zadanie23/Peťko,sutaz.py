krajiny=[]
pocet=[]
body=0
sutaziaci=[]
vitaz=''
with open('zadanie23/skok_do_dialky','r') as file:
    for line in file:
        line=line.strip().split()
        sutaziaci.append(line)
        if line[1] in krajiny:
            for i in range(len(krajiny)):
                if line[1] == krajiny[i]:
                    pocet[i] += 1
        else:
            krajiny.append(line[1])
            pocet.append(1)
        for i in line[2:]:
            if int(i) >= body:
                body=int(i)

for i in range(len(sutaziaci)):
    if str(body) in sutaziaci[i]:
        vitaz += sutaziaci[i][0]+' '

for i in range(len(pocet)):
    print(str(pocet[i])+'x '+krajiny[i])
print('vitaz/vitazi:'+vitaz)