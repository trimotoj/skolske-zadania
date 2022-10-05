lower_letters=[0]*(ord('z')-ord('a')+1)
upper_letters=[0]*(ord('Z')-ord('A')+1)
number_of_letters=0
number_of_all_letters=0
j=1
subor=input('Zadaj nazov suboru, ktory chces otvorit (mor_ho/vety) : ')
file2=open('ZOZNAM.txt','w')
with open('zadanie5/'+subor+'.txt','r') as file:
    for line in file:
        line=line.strip()
        for letter in line:
            if letter != ' ':
                if ord(letter) > ord('Z'):
                    i = ord(letter) - ord('a')
                    lower_letters[i]+=1
                else:
                    i = ord(letter) - ord('A')
                    upper_letters[i]+=1
                number_of_letters+=1       
        file2.write('Pocet pismen v '+str(j)+'.riadku: '+str(number_of_letters)+'\n')
        for i in range(len(lower_letters)):
            if upper_letters[i] != 0:
                file2.write((chr(i+65)+' - '+str(upper_letters[i])+'x')+'\n')
            if lower_letters[i] != 0:
                file2.write((chr(i+97)+' - '+str(lower_letters[i])+'x')+'\n')
        lower_letters=[0]*(ord('z')-ord('a')+1)
        upper_letters=[0]*(ord('Z')-ord('A')+1)
        j+=1
        number_of_all_letters+=number_of_letters
        number_of_letters=0
    file2.write('Pocet pismen spolu: '+str(number_of_all_letters))    
file2.close()
