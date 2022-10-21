import tkinter

window = tkinter.Tk()
window.title("Zneskodni bombu!")
window.resizable(False, False)

canvas = tkinter.Canvas(width=300, height=300)

canvas.pack()
window.mainloop()
