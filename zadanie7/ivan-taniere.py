import tkinter
import random

window = tkinter.Tk()
window.title("Najdi puknuty tanier")
window.resizable(False, False)

taniere = "ABCDEFGHIJ"
puknutyTanier = random.choice(taniere)
print(puknutyTanier)
kliknuteTaniere = []


def tanier(startX, text):
    canvas.create_oval(startX + 5, 5, startX + 98, 98, width=3, fill="blue", tags=text)
    canvas.create_oval(startX + 20, 20, startX + 83, 83, width=2, fill="blue", tags=text)
    canvas.create_text(startX + 50, 50, text=text, fill="white", font=("Arial", 35), tags=text)


def click(event):
    vybratyTanier = canvas.gettags("current")
    if vybratyTanier == ():
        return
    elif vybratyTanier[0] == puknutyTanier:
        canvas.delete("all")
        canvas.create_text((len(taniere) * 100) / 2, 40, text=f"Gratulujem, oznacil si puknuty tanier {puknutyTanier}!", fill="blue", font=("Arial", 15))
        canvas.create_text((len(taniere) * 100) / 2, 60, text=f"Viackrat si klikol na taniere:{''.join(list(set([i for i in kliknuteTaniere if kliknuteTaniere.count(i) >= 2])))}", fill="red", font=("Arial", 15))
    else:
        kliknuteTaniere.append(vybratyTanier[0])


canvas = tkinter.Canvas(height=100, width=len(taniere) * 100)
canvas.pack()

for index, value in enumerate(taniere):
    tanier(index * 100, value)

canvas.bind("<Button-1>", click)

window.mainloop()
