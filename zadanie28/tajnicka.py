def draw():
    global x, y
    x = 200
    x -= (int(line[0])-1)*(2*r)
    for i in range(len(line[1])):
        farba='white'
        if i == int(line[0])-1:
            farba='gray'
        canvas.create_rectangle(x-r,y-r,x+r,y+r,fill=farba)
        canvas.create_text(x,y,text=line[1][i])
        x+= 2*r
    y += 2*r

y=50
r=10
import tkinter
canvas=tkinter.Canvas()
canvas.pack()
with open('zadanie28/vstup','r') as file:
    for line in file:
        line=line.split()
        draw()

canvas.mainloop()