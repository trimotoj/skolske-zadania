import tkinter
import random

window = tkinter.Tk()
window.title("Zneskodni bombu!")
window.resizable(False, False)

farby = list(set(["green", "red", "grey", "blue", "yellow"]))
spravnyKablik = random.choice(farby)
print(spravnyKablik)
cas = 5
skonci = False


def kablik(startY, farba):
    canvas.create_line(50, startY + 70, 250, startY + 70, width=10, fill=farba, tags=farba)


def click(event):
    global skonci
    vybratyKablik = canvas.gettags("current")
    if vybratyKablik == ():
        return
    elif vybratyKablik[0] == spravnyKablik:
        canvas.create_text(200, 90 + len(farby) * 10, text="Vyhral si!", font=("Arial", 25))
        skonci = True


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


canvas = tkinter.Canvas(width=400, height=110 + len(farby) * 10)
canvas.create_text(200, 25, text="Pyrotechnik", fill="blue", font=("Arial", 17))
canvas.create_text(200, 45, text="oznac spravny kablik", font=("Arial", 10))

for index, value in enumerate(farby):
    kablik(index * 10, value)

timer = canvas.create_text(300, 88, text=cas, fill='red', font=("Arial", 30))

casovac()

canvas.bind("<Button-1>", click)

canvas.pack()
window.mainloop()
