import tkinter, random
canvas = tkinter.Canvas(width=700, height=800)
canvas.pack()

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)


def animacia():
    canvas.delete('all')
    canvas.create_line(650,0,650,800,fill='red',width=2)
    y = 25
    for lodka in range(15):
        x = pozicieX[lodka]
        x+=random.randint(1,10)
        lodicka(x,y)
        y+=55
        pozicieX[lodka] = x
    for i in range(len(pozicieX)):    
        if pozicieX[i] >= 630:
            canvas.create_text(350,400,text='Vyhrala lodicka cislo: '+str(i+1),font='Arial 20',fill='red')
            return
            
    canvas.after(20,animacia)

def klik(event):
    animacia()    


pozicieX=[]
x , y = 20 , 25
for lodka in range(15):
    lodicka(x,y)
    y+=55
    pozicieX.append(x)
print(pozicieX)
canvas.create_line(650,0,650,800,fill='red',width=2)
canvas.bind('<Button-1>',klik)
canvas.mainloop()

