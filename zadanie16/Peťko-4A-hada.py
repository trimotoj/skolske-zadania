games=0
lenght=0
file2=open('zadanie16/hada2','w')
with open('zadanie16/hada','r') as file:
    for line in file:
        line=line.strip()
        games+=1
        pocet=1
        if len(line) > lenght:
            lenght= len(line)
        for i in range(len(line)-1):
            if line[i+1] == line[i]:
                pocet+=1
            else:
                file2.write(line[i]+' '+str(pocet)+' ')
                pocet=1
        file2.write(line[i+1]+' '+str(pocet)+'\n')
print('Pocet hier:',games)
print('Najdlhsia hra:',lenght)