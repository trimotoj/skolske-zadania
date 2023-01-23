import tkinter, random
canvas = tkinter.Canvas(width=400, height=150)
canvas.pack()

farby=('green','red','gray','blue','yellow')

def kablik(x,y):
    canvas.create_rectangle(x,y,x+200,y+10,width=2,fill=farby[kabel])

def ziskaj_suradnice(s):
    x = s.x
    y = s.y
    klik(surKablika)


def klik(surKablika):
    if surKablika[spravnyKablik][0] <= x <= surKablika[spravnyKablik][2] and surKablika[spravnyKablik][1] <= y <= surKablika[spravnyKablik][3]:
        canvas.create_text(200,120,text='Vyhral si',font='Arial 20', fill='blue')    

def casovac():
    global cas
    if cas >= 0:
        canvas.itemconfigure(timer, text=cas)
        cas -= 1
        if not skonci:
            canvas.after(1000, casovac)
    else:
        canvas.delete("all")
        canvas.unbind('<Button-1>')        

#---------------------------------------------------
cas = 5
skonci = False
spravnyKablik=random.randint(1,len(farby))
surKablika=()
timer = canvas.create_text(300, 80, text=cas, fill='red', font=("Arial", 30))
x , y = 50 , 50
for kabel in range(len(farby)):
    kablik(x,y)
    surKablika+=(x,y,x+200,y+10),
    y+=10
    
casovac()
canvas.create_text(200,20,text='Pyrotechnik',font='Arial 15',fill='blue')
canvas.create_text(200,35,text='oznac spravny kablik')
canvas.bind('<Button-1>',ziskaj_suradnice)
print(farby[spravnyKablik])
canvas.mainloop()