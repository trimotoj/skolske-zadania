import tkinter
#
def kresli(file):
    global y, obrazok
    for line in file:
        x=0
        line=line.strip().split()
        for number in line:
            if number == '0':
                canvas.create_rectangle(x,y,x+10,y+10,fill='black',outline='')
            obrazok.append(number)
            x+=10
        y+=10
#
def komprimuj(obrazok):
    global pocet, subor
    subor=open('KOMPRIM.txt','w')
    subor.write(str(rozmery[0])+' '+str(rozmery[1])+'\n')
    subor.write(obrazok[0]+' ')
    for i in range(len(obrazok)-1):
        if obrazok[i] == obrazok[i+1]:
            pocet+=1
        else:
            subor.write(str(pocet)+' ')
            pocet=1
    subor.write(str(pocet))
#------------------------------------------------------------
y=0
pocet=1
obrazok=[]
with open('zadanie13/obrazok.txt') as file:
    rozmery=file.readline().strip().split()
    sirka, vyska = int(rozmery[0])*10, int(rozmery[1])*10
    canvas=tkinter.Canvas(width=sirka,height=vyska,bg='white')
    kresli(file)
    komprimuj(obrazok)
    subor.close()

canvas.pack()
canvas.mainloop()






