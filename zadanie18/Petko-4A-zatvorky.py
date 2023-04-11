import tkinter
w=700
h=150
canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()


vyraz='((a+b)*2+(((c+d)-2*a)+b)*(e+f)*2)'
farby=['red','green','blue','yellow','purple','violet']
pocitadlo = -1


x=10
y=25

for i in vyraz:
    if i == '(':
        pocitadlo += 1
        farba = farby[pocitadlo]
        canvas.create_text(x,y,text=i,fill=farba,font='Arial 30')

    elif i == ")":
        farba = farby[pocitadlo]
        canvas.create_text(x,y,text=i,fill=farba,font='Arial 30')
        farby.pop(pocitadlo)
        pocitadlo -= 1

    else:
        canvas.create_text(x,y,text=i,font='Arial 30') 
    x+=20

canvas.mainloop()