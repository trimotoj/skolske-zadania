import tkinter
import random

window = tkinter.Tk()
window.title("preteky lodiek")
window.resizable(False, False)

canvas = tkinter.Canvas(width=700, height=550)
canvas.pack()


def lodicka(x, y, index):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y - 25, x + 10 + plachta, y - 10, x, y - 5, tags=f"lodka{index}")
    canvas.create_polygon(x - 20, y, x + 20, y, x + 10, y + 8, x - 10, y + 8, tags=f"lodka{index}")


def nahodnyPosun() -> int:
    return random.randint(1, 10)


def click(event):
    canvas.unbind("<Button-1>")
    pohyb()


def pohyb():
    for i in range(15):
        prevLoc = canvas.coords(f"lodka{i+1}")
        canvas.delete(f"lodka{i+1}")
        lodicka(int(prevLoc[0]) + nahodnyPosun(), int(prevLoc[1]), i + 1)
        x1, y1, x2, y2 = [int(i) for i in canvas.coords(ciel)]
        coll = canvas.find_overlapping(x1, y1, x2, y2)
        coll = list(coll)
        coll.remove(ciel)
        if len(coll) != 0:
            lodka = "".join(canvas.gettags(coll[0]))
            canvas.create_text(350, 275, text=f"Vyhrala lodicka cislo: {''.join([lodka[i] for i in range(len(lodka)) if lodka[i].isdigit()])}", fill="red", font=("Arial", 25))
            return
    canvas.after(10, pohyb)


for i in range(15):
    lodicka(25, i * 36 + 36, i + 1)

ciel = canvas.create_line(650, 0, 650, 550, fill="red", width=5)

canvas.bind("<Button-1>", click)

window.mainloop()
