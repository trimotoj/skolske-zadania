import tkinter

y=0

with open('zadanie13/obrazok.txt') as file:
    rozmery = file.readline().strip().split()
    w, v = int(rozmery[0]), int(rozmery[1])
    canvas = tkinter.Canvas(width=w*10, height=v*10,bg='white')
    for line in file:
        x=0
        line=line.strip().split()
        for number in line:
            if number == '0':
                farba='black'
                canvas.create_rectangle(x*10,y*10,x*10+10,y*10+10,fill=farba,outline='')
            x+=1
        y+=1

canvas.pack()
canvas.mainloop()