def vajce():
    canvas.create_oval(x-10,y-15,x+10,y+15,tags='vajce')

def pohyb():
    global y
    canvas.delete('vajce')
    y+=3
    vajce()
    if y > (HEIGHT-HEIGHT/3):
        canvas.create_text(x,y,text=chr(pismeno),font='Arial 15',tags='vajce')
    if y >= HEIGHT+15:
        canvas.create_text(WIDTH//2,HEIGHT//2,text='PREHRAL SI',font='Arial 50')
        return
    canvas.after(10,pohyb)

def stlac(event):
    global pismeno, x, y
    if event.keysym == chr(pismeno):
        y=15
        x=random.randint(10,WIDTH-10)
        pismeno=random.randint(ord('a'),ord('z'))



import tkinter, random
WIDTH=500
HEIGHT=500
canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT)
canvas.pack()
#================================================
y=15
x=random.randint(10,WIDTH-10)
pismeno=random.randint(ord('a'),ord('z'))
pohyb()
canvas.bind_all('<Key>',stlac)
canvas.mainloop()