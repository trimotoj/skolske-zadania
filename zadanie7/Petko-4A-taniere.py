import random
import tkinter
pocetTanierov=5
w, h =(pocetTanierov*100)+(pocetTanierov-2)*10+(15) , 105
canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()

def klik(suradnice):
    global pocet , duplikaty
    x = suradnice.x
    y = suradnice.y
    if suradniceTanierov[vybranyTanier][2] >= x >= suradniceTanierov[vybranyTanier][0] and suradniceTanierov[vybranyTanier][3] >= y >= suradniceTanierov[vybranyTanier][1] :
        canvas.delete('all')
        canvas.create_text(w//2,h//2,text='Gratulujem, oznacil si puknuty tanier')
        for i in kliknuteTaniere:
            if kliknuteTaniere.count(i) >= 2:
                duplikaty.append(i)
        duplikaty=list(set(duplikaty))
        canvas.create_text(pocetTanierov * 100 / 2, 60, text="Viackrat si klikol na taniere: "+''.join(duplikaty), fill="red", font=("Arial", 15))
    else:
        for i in range(len(suradniceTanierov)):
            if suradniceTanierov[i][2]  >= x >= suradniceTanierov[i][0] and suradniceTanierov[i][3]  >= y >= suradniceTanierov[i][1]:
                kliknuteTaniere.append(chr(i+65))
                print(kliknuteTaniere)
                


kliknuteTaniere=[]
duplikaty=[]
suradniceTanierov=()
pocet=()
x=y=5
for i in range(pocetTanierov):
    canvas.create_oval(x,y,x+100,y+100,fill='blue',width=3)
    canvas.create_oval(x+20,y+20,x+80,y+80)
    canvas.create_text(x+50,y+50,text=chr(i+65),font='Arial 25',fill='white')
    suradniceTanierov+=(x+20,y+20,x+80,y+80),
    x+=110
    
vybranyTanier=random.randrange(len(suradniceTanierov))
print(chr(vybranyTanier+65))
canvas.bind('<Button-1>',klik)
canvas.mainloop()