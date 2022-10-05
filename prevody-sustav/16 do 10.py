hexnumber='FF'
decnumber=0
lenght=len(hexnumber)
for i in hexnumber:
    if i in 'ABCDEF':
        cislo=ord(i)+5-60
        decnumber+=(cislo)*(16**(lenght-1))
    else:
        decnumber+=int(i)*(16**(lenght-1))  
    lenght-=1

print(decnumber)  
   
