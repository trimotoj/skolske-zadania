with open('zadanie10/VYSLEDZNAMKA.txt','r') as file:
    subor=open('zadanie10/VYSVEDCENIE.txt','w')
    for line in file:
        sucet_znamok=0
        line=line.strip().split()
        for znamka in line[-1:1:-1]:
            sucet_znamok+=int(znamka)
        if sucet_znamok/(len(line)-2) - sucet_znamok//(len(line)-2) >= 0.5:
            subor.write(line[1]+' '+line[0]+' '+str(sucet_znamok//(len(line)-2)+1)+'\n')
        else:
            subor.write(line[1]+' '+line[0]+' '+str(sucet_znamok//(len(line)-2))+'\n')
subor.close()
        

