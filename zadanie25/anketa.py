def draw(event):
    y=30
    canvas.delete('a')
    if event.keysym == '1':
        pocet[0] += 1
    if event.keysym == '2':
        pocet[1] += 1
    if event.keysym == '3':
        pocet[2] += 1
    with open('zadanie25/anketa','w',encoding='utf-8') as file2:
        file2.write(file[0])
        for i in range(3):
            if pocet[i] == max(pocet):
                farba='green'
            else:
                farba='red'
            canvas.create_text(5,y,text=str(i+1)+')'+' '+odpovede[i]+' - '+str(pocet[i]),anchor="w",tags='a')
            canvas.create_line(100,y,100+pocet[i]*2,y,fill=farba,width=15,tags='a') 
            y+=20
            file2.write(str(pocet[i])+' ')
        

import tkinter
canvas=tkinter.Canvas()
canvas.pack()


x=125
y=20
odpovede=['Ano','Nie','Neviem']
with open('zadanie25/anketa','r+',encoding='utf-8') as file:
    file=file.readlines()
    otazka=file[0]
    canvas.create_text(x,y,text=otazka)
    pocet=file[1].split()
    y+=10
    for i in range(len(pocet)):
        pocet[i] = int(pocet[i])
    for i in range(3):
        if pocet[i] == max(pocet):
             farba='green'
        else:
             farba='red'
        canvas.create_text(5,y,text=str(i+1)+')'+' '+odpovede[i]+' - '+str(pocet[i]),anchor="w",tags='a')
        canvas.create_line(100,y,100+pocet[i]*2,y,fill=farba,width=15,tags='a')
        y+=20

canvas.bind_all('<Key>',draw)
canvas.mainloop()