import tkinter
w=700
h=150
canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()


vyraz='((a+b)*2+(((c+d)-2*a)+b)*(e+f)*2)'
zatvorky=''
for i in vyraz:
    if i in '()':
        zatvorky+=i
farby=('red','green','blue','yellow','purple','violet')
x=10
y=25
a=0
dlzka_zatvoriek=0
for i in range(len(vyraz)):
    if vyraz[i] in '()':
        dlzka_zatvoriek+=1
    if dlzka_zatvoriek == len(zatvorky):
        canvas.create_text(x,y,text=vyraz[i],fill=farby[0],font='Arial 30')
        dlzka_zatvoriek=0
    elif vyraz[i] == '(':
        canvas.create_text(x,y,text=vyraz[i],fill=farby[a],font='Arial 30')
        a+=1
        b=a
    elif vyraz[i] == ')':
        b-=1
        canvas.create_text(x,y,text=vyraz[i],fill=farby[b],font='Arial 30')
    else:
        canvas.create_text(x,y,text=vyraz[i],font='Arial 30')
    x+=20

if len(zatvorky) % 2 == 0 or zatvorky[-1] == '(':
    canvas.create_text(w//2,y+75,text='Uzátvorkovanie je správne',font='Ariel 30')

else:
    canvas.create_text(w//2,y+75,text='Uzátvorkovanie je nesprávne',font='Ariel 30')



canvas.mainloop()