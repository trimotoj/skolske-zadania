
def animacia():
    global y, slovo
    canvas.delete('slovo')
    slovo=''.join(slovo)
    canvas.create_text(x,y,text=slovo,font='Arial 20',tags='slovo')
    y+=1
    if '*' not in slovo:
        return
    canvas.after(10,animacia)

def stlac(event):
    global slovo, word
    slovo=list(slovo)
    if event.keysym in word:
        for i in range(len(word)):
            if event.keysym == word[i]:
                slovo[i]=word[i]
#-----------------------------------------------------------------
import random, tkinter
WIDTH=500
HEIGHT=500
canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT)
canvas.pack()

words=[]
with open('zadanie31/vstup') as file:
    for line in file:
        words.append(line.strip())

word=random.choice(words)
print(word)
slovo='*'*len(word)
x=random.randint(0,WIDTH-50)
y=0
animacia()

canvas.bind_all('<Key>',stlac)
canvas.mainloop()



