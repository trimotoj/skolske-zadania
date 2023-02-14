decnumber=123
binnumber=''
while decnumber != 0:
    if decnumber % 2 == 1:
        binnumber+='1'
    else:
        binnumber+='0'
    decnumber=decnumber//2

print(binnumber[::-1])
