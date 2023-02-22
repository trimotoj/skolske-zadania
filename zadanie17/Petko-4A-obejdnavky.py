pocet_objednavok=0
jedla=['z','c','m','o']
pocet_jedal=[0]*len(jedla)
dostatocny_pocet_jedal=''
nedostatocny_pocet_jedal=''

with open('zadanie17/objednane_jedla.txt','r') as file:
    for line in file:
        line=line.strip()
        for i in range(len(jedla)):
            if line[-1] == jedla[i]:
                pocet_jedal[i] += 1
        pocet_objednavok+=1

    for i in range(len(pocet_jedal)):
        if pocet_jedal[i] >= 20:
            dostatocny_pocet_jedal+=jedla[i]+' '
        else:
            nedostatocny_pocet_jedal+=jedla[i]+' '

    print('Počet objednaných jedál:',pocet_objednavok)
    print('------')

    for i in range(len(jedla)):
        print(str(pocet_jedal[i])+'x',jedla[i])
        
    print('------')
    print('Jedlá s dostatočným množstvom objednávok: '+dostatocny_pocet_jedal)
    print('Jedlá s nedostatočným množstvom objednávok: '+nedostatocny_pocet_jedal)
    