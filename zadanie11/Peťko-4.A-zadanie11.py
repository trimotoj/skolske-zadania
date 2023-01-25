def notova_osnova():
    global y
    for linajka in range(5):
        canvas.create_line(0,y,0+sirka,y)
        y+=10

def draw(skladba,noty):
    global y, xnoty
    for nota in skladba:
        if xnoty > sirka-10:
            xnoty=10
            y+=25
            notova_osnova()
        for i in range(len(noty)):
            if nota == noty[i]:
                ynoty=(y-5)-(i*5)
                canvas.create_oval(xnoty,ynoty,xnoty+10,ynoty+10)
                xnoty+=25


#==============================================================
import tkinter, random
sirka, vyska = 350, 150
canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()
#
skladba=open('zadanie11/skladba.txt','r').read().strip()
noty=open('zadanie11/noty.txt','r').read().strip().split()
#
y=xnoty=10
#
notova_osnova()
draw(skladba,noty)

canvas.mainloop()





