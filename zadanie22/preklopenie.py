import tkinter
with open('zadanie22/obrazok','r') as file:
    rozmery=file.readline().strip().split()
    WIDTH=int(rozmery[0])*2
    HEIGHT=int(rozmery[1])
    canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT,bg='white')
    subor=[]
    y=0
    for line in file:
        x=0
        line=line.strip()
        subor.append(line)
        for number in line:
            if number == '1':
                canvas.create_rectangle(x,y,x+1,y+1)
            x+=1
        y+=1

def preklop():
    global x, y
    canvas.delete('all')
    y=0
    for line in range(len(subor)):
        subor[line]=subor[line][-1::-1]
        x=0
        for number in subor[line]:
            if number == '1':
                canvas.create_rectangle(x,y,x+1,y+1)
            x+=1
        y+=1

    
button1 = tkinter.Button(text='PREKLOP',command=preklop) 
button1.pack()
canvas.pack()
canvas.mainloop()
