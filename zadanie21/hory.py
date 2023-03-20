import tkinter, random
WIDTH=800
HEIGHT=500
canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT,bg='lightblue')

def stlac(event):
    canvas.delete('all')
    farba=['blue','green','lightgreen','SeaGreen3']
    prava_strana=()
    for j in range(5):
        VRCH_X=hora_x=random.randint(0,WIDTH)
        VRCH_Y=hora_y=random.randint(0,HEIGHT)
        hora=(VRCH_X,VRCH_Y)
        for i in range((VRCH_X//10)+1):
            if VRCH_Y < HEIGHT//2:
                hora_y=random.randint(hora_y,hora_y+10)
            else:
                hora_y=random.randint(hora_y-10,hora_y)
            hora_x-=10
            hora+=(hora_x,hora_y)
        hora_y=VRCH_Y
        hora_x=VRCH_X
        hora+=(0,HEIGHT,WIDTH,HEIGHT)
        for i in range(((WIDTH-VRCH_X)//10)+1):
            if VRCH_Y < HEIGHT//2:
                hora_y=random.randint(hora_y,hora_y+10)
            else:
                hora_y=random.randint(hora_y-10,hora_y)
            hora_x+=10
            prava_strana+=(hora_y,hora_x)
        hora+=prava_strana[-1:1:-1]
        canvas.create_polygon(hora,fill=farba[random.randrange(4)])
        hora=()
        prava_strana=()  

canvas.bind_all('<space>',stlac)
canvas.pack()
canvas.mainloop()