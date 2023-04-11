objednane_jedla=0
jedla=[]
pocet=[]
dostatok=''
nedostatok=''
with open('zadanie17/objednane_jedla.txt','r') as file:
    for line in file:
        objednane_jedla+=1
        line=line.split()
        for i in range(len(jedla)):
            if jedla[i] == line[1]:
                pocet[i] +=1
        if line[1] not in jedla:
            jedla.append(line[1])
            pocet.append(1)
            
print('Pocet objednanych jedal:',objednane_jedla)

for i in range(len(jedla)):
    print(str(pocet[i])+'x'+' '+jedla[i])
    if pocet[i] >= 20:
        dostatok += str(jedla[i])+' '
    else:
        nedostatok += str(jedla[i])+' '

print('dostatok: '+dostatok)
print('nedostatok: '+nedostatok)



