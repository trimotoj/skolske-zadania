pocet_hier=0
najdlhsia_hra=0

with open('zadanie16/hada.txt','r') as file:
    komprim=open('zadanie16/komprim.txt','w')
    for line in file:
        line=line.strip()
        hra=pocet=1
        for i in range(1,len(line)):
            if line[i] == line[i-1]:
                pocet+=1
            else:
                komprim.write(line[i-1]+str(pocet)+' ')
                pocet = 1
            hra+=1
        if najdlhsia_hra < hra:
            najdlhsia_hra = hra
        pocet_hier+=1
        komprim.write(line[i]+str(pocet))
        komprim.write('\n')

print('pocet hier:',pocet_hier)
print('najdlhsia hra:',najdlhsia_hra)