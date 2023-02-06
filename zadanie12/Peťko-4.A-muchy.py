def pohyb():
    global muchaX, muchaY, x ,y
    canvas.delete('mucha')
    for i in range(len(muchaX)):
        canvas.create_oval(muchaX[i],muchaY[i],muchaX[i]+5,muchaY[i]+5,tags='mucha')
        if vylet==0:
            if x+200-5 <= muchaX[i]:
                muchaX[i] -= 2
            elif x+5 >= muchaX[i]:
                muchaX[i] += 2
            elif y+200-5 <= muchaY[i]:
                muchaY[i] -= 2
            elif y+5 >= muchaY[i]:
                muchaY[i] += 2
            else:
                muchaX[i] += random.randint(-2,2)
                muchaY[i] += random.randint(-2,2)
        else:
             muchaX[i] += random.randint(-2,2)
             muchaY[i] += random.randint(-2,2)
    canvas.after(1,pohyb)
    
def von():
    global klietka, vylet
    canvas.delete('klietka')
    vylet=1
    

sirka, vyska = 500, 500
pocet = 100
muchaX=[sirka//2]*pocet
muchaY=[vyska//2]*pocet
x, y = 150, 150
vylet=0

import tkinter, random
canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()
canvas.create_rectangle(x,y,x+200,y+200,tags='klietka')

pohyb()
button1 = tkinter.Button(text='VON', command=von)
button1.pack()

canvas.mainloop()