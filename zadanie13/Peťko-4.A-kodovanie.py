# import tkinter

# y=0

# with open('zadanie13/obrazok.txt') as file:
#     rozmery = file.readline().strip().split()
#     w, v = int(rozmery[0]), int(rozmery[1])
#     canvas = tkinter.Canvas(width=w*10, height=v*10,bg='white')
#     for line in file:
#         line=line.strip().split()
#         x=0
#         for number in line:
#             if number == '0':
#                 canvas.create_rectangle(x*10,y*10,x*10+10,y*10+10,fill='black',outline='')
#             x+=1
#         y+=1

# canvas.pack()
# canvas.mainloop()

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
    komprimuj(obrazok)


def komprimuj(obrazok):
    global pocet, komprim
    komprim=open('KOMPRIM.txt','w')
    komprim.write(str(rozmery[0])+' '+str(rozmery[1])+'\n')
    komprim.write(obrazok[0]+' ')
    for i in range(len(obrazok)-1):
        if obrazok[i] == obrazok[i+1]:
            pocet+=1
        else:
            komprim.write(str(pocet)+' ')
            pocet=1
    komprim.write(str(pocet))
    

import tkinter
y=0
pocet=1
obrazok=[]
with open('zadanie13/obrazok.txt') as file:
    rozmery=file.readline().strip().split()
    sirka, vyska = int(rozmery[0])*10, int(rozmery[1])*10
    canvas=tkinter.Canvas(width=sirka,height=vyska,bg='white')
    kresli(file)
    komprim.close()

canvas.pack()
canvas.mainloop()






