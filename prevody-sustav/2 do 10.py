binnumber='1110001010011'
decnumber=0
lenght=len(binnumber)
for i in binnumber:
    if i == '1':
        decnumber+=2**(lenght-1)
    lenght-=1
print(decnumber)