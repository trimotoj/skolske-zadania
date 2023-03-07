def zrut():
    canvas.create_oval(xz,yz,xz+rz,yz+rz,fill='blue',tags='zrut')

def jablcka(pocet):
    
    for i in range(pocet):
        xj=random.randint(xz+rz+1,w-rj-1)
        yj=random.randint(yz+rz+1,h-rj-1)
        canvas.create_oval(xj-rj,yj-rj,xj+rj,yj+rj,fill='red')
        suradnice_jablcok.append((xj,yj))


def pohyb():
    global xz,yz
    canvas.delete('zrut')
    xz+=xp
    yz+=yp
    zrut()
    canvas.after(20,pohyb)

def zmena_smeru(event):
    global xp,yp
    if event.keysym == 'w':
        xp=0
        yp=-1
    if event.keysym == 'a':
        xp=-1
        yp=0
    if event.keysym == 's':
        xp=0
        yp=1
    if event.keysym == 'd':
        xp=1
        yp=0


import tkinter, random
w=h=500
canvas=tkinter.Canvas(width=w,height=h)

xz=yz=5
xp=1
yp=0
rz=50
rj=10
suradnice_jablcok=[]
jablcka(10)
pohyb()
canvas.bind_all('<Key>',zmena_smeru)

print(suradnice_jablcok)
canvas.pack()
canvas.mainloop()