import tkinter
import random

window = tkinter.Tk()
window.title("preteky lodiek")
window.resizable(False, False)

canvas = tkinter.Canvas(width=700, height=550)
canvas.pack()


def lodicka(x, y, index):
    plachta = random.randint(-3, 3)
    canvas.create_line(
        x, y, x, y - 25, x + 10 + plachta, y - 10, x, y - 5, tags=f"lodka{index}"
    )
    canvas.create_polygon(
        x - 20, y, x + 20, y, x + 10, y + 8, x - 10, y + 8, tags=f"lodka{index}"
    )


def nahodnyPosun() -> int:
    return random.randint(50, 100)


def click(event):
    # print(canvas.gettags("current"))
    # canvas.unbind("<Button-1>")
    for i in range(15):
        # print(canvas.coords("ciel"))
        prevLoc = canvas.coords(f"lodka{i}")
        canvas.delete(f"lodka{i}")
        lodicka(int(prevLoc[0]) + nahodnyPosun(), int(prevLoc[1]), i)
        # x1, y1, x2, y2 = [int(i) for i in canvas.coords("ciel")]
        coll = canvas.find_overlapping(200, 200, 400, 400)
        coll = list(coll)
        # coll.remove(player)
        # if len(coll) != 0:
        #     print(canvas.gettags("current")"hit")


for i in range(15):
    lodicka(25, i * 36 + 36, i)

canvas.create_line(650, 0, 650, 550, fill="red", width=5, tags="ciel")
# canvas.create_rectangle(200, 200, 400, 400)

canvas.bind("<Button-1>", click)

window.mainloop()
