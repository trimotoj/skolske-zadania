def direction(event):
    global xp, yp
    if event.keysym=='w':
        yp=-1
        xp=0
    if event.keysym=='a':
        xp=-1
        yp=0
    if event.keysym=='s':
        yp=1
        xp=0
    if event.keysym=='d':
        xp=1
        yp=0

def draw():
    global x, y
    x+=xp
    y+=yp
    canvas.create_rectangle(x,y,x,y)
    if [x,y] in suradnice:
        canvas.create_text(WIDTH//2,HEIGHT//2,text='NARAZIL SI',font="Arial 50",fill='red')
        return
    else:
        suradnice.append([x,y])
    canvas.after(10,draw)


import tkinter
WIDTH,HEIGHT=500,500

canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT)
canvas.pack()

x=WIDTH//2
y=HEIGHT//2
xp=0
yp=-1
suradnice=[]

draw()
canvas.bind_all('<Key>',direction)
canvas.mainloop()