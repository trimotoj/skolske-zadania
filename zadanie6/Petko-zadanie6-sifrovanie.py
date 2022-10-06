zoznam_pismen=['ABC','DEF','GHI','JKL','MNO','PQR','STU','VWX','YZ']
veta=input('Zadaj vetu na sifrovanie: ')
veta=veta.upper()
zasifrovana_veta=''
pocet=[0]*10
for pismeno in veta:
	if pismeno == ' ':
		zasifrovana_veta+='0'+' '
	for i in range(len(zoznam_pismen)):
		if pismeno in zoznam_pismen[i]:
			for j in range(len(zoznam_pismen[i])):
				if pismeno == zoznam_pismen[i][j]:
				    zasifrovana_veta+=(j+1)*str(i+1)+' '
print(zasifrovana_veta)
for i in range(10):
    pocet[i]=zasifrovana_veta.count(str(i))
najvacsie_cislo=max(pocet)
print('Najvyskytovanejsie cisla: ',end='')
for i in range(10):
    if pocet[i] == najvacsie_cislo:
        print(i,end=' ')
