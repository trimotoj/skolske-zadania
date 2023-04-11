def prva(event):
    pohyb()
    
def pohyb():
    global x
    canvas.delete('zastavka')
    x-=1
    canvas.create_text(x,y,text=zastavky[i],font='Arial 30',tags='zastavka')
    if x < w/2:
        canvas.create_text(x+w,y,text=zastavky[i],font='Arial 30',tags='zastavka')
    if x+w == w/2:
        x=w/2
    canvas.after(10,pohyb)

def dalsia(event):
    global i
    i += 1
    if i == len(zastavky):
        i = 0
    if i == len(zastavky) - 1:
        canvas.create_text(w/2,h-20,text='POSLEDNA ZASTAVKA, PROSIM VYSTUPTE!!!',fill='red',font='Arial 15',tags='oznam')

    else:
        canvas.delete('oznam')

#===============================================================    
zastavky=[]
w=500
h=100
i=0
x=w/2
y=h/2
#------------------------------------------------------------------

with open('zadanie4/zastavky.txt','r',encoding='utf-8') as file:
    for line in file:
        line=line.strip()
        zastavky.append(line)
    
import tkinter
canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()
 
canvas.create_text(x,y,text=zastavky[0],font='Arial 30',tags='zastavka')

canvas.bind_all('<Return>',prva)
canvas.bind_all('<Key>',dalsia)
canvas.mainloop()