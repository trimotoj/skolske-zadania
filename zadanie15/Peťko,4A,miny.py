import tkinter, random
sirka, vyska = 500, 500
canvas=tkinter.Canvas(width=sirka,height=vyska)
canvas.pack()

def miny(pocet):
    global xsur, ysur, subor
    for i in range(pocet):
        x=random.randint(0,sirka-10)
        y=random.randint(0,vyska-10)
        canvas.create_oval(x,y,x+10,y+10,fill='black')
        xsur.append(x)
        ysur.append(y)
        subor.write(str(x)+' '+str(y)+'\n')
    subor.close()

def pohyb(s):
    global zrus,subor2
    if zrus == 0:
        x=s.x
        y=s.y
        subor2.write(str(x)+' '+str(y)+'\n')
        canvas.create_rectangle(x,y,x+2,y+2,fill='black')
        for i in range(len(xsur)):
            if xsur[i]+10 >= x >= xsur[i] and ysur[i]+10 >= y >= ysur[i]:
                canvas.create_oval(xsur[i],ysur[i],xsur[i]+10,ysur[i]+10,fill='red',outline='')
                canvas.create_text(sirka//2,vyska//2,text='PREHRAL SI',font='Ariel 50')
                zrus=1
#===============================================================
pocet=10
xsur=[]
ysur=[]
zrus=0
subor=open('MINY.txt','w')
subor2=open('CESTA.txt','w')
miny(pocet)
canvas.bind('<B1-Motion>',pohyb)
canvas.mainloop()
