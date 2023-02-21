def vyber(s):
    kod = entry1.get()
    if kod != '' and kod.isdigit():
        xk=s.x
        yk=s.y
        if y <= yk <= y+100: 
            i=xk//100
            subor=open('vyber_jedla.txt','a')
            subor.write(kod+' '+farby[i]+'\n')
            subor.close()
            pocet[i]+=1
            for i in range(len(pocet)):
                print(str(pocet[i])+'x ',farby[i])
            print('--------')
#-------------------------------------------------------------
x=0
y=50

import tkinter
w, h = 400, 200
canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()

canvas.create_text(w//2,25,text='VYBER JEDLA',font='Arial 20',fill='red')
farby=('green','red','blue','yellow')
pocet=[0]*4
for i in range(len(farby)):
    canvas.create_rectangle(x,y,x+100,y+100,fill=farby[i],outline='')
    x+=100

subor=open('zadanie14/vyber_jedla.txt','w')
subor.close()

canvas.bind('<Button-1>', vyber)
label = tkinter.Label(text='kod studenta')
label.pack()
entry1 = tkinter.Entry()
entry1.pack()

canvas.mainloop()