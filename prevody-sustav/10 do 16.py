decnumber=563978
hexnumber=''
while decnumber != 0:
    cislo=decnumber % 16
    if cislo <= 9:
        hexnumber+=str(cislo)
    else:
        cislo+=55
        hexnumber+=chr(cislo)
    decnumber=decnumber//16
print(hexnumber[::-1])