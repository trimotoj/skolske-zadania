import tkinter
import random
w = h = 500
canvas = tkinter.Canvas(width=w, height=h)
canvas.pack()


def pohyb():
    global xZrut, yZrut
    canvas.delete('zrut')
    xZrut += xPosun
    yZrut += yPosun
    canvas.create_oval(xZrut, yZrut, xZrut+r,yZrut+r, fill='blue', tags='zrut')
    for i in range(len(sur)):
        if  xZrut+r >= sur[i][0]+rj and xZrut >= sur[i][1]:
            if yZrut+r >= sur[i][1]+rj and yZrut >= sur[i][1]:
                canvas.delete(str(i+2))

    # for i in range(len(sur)):
    # if sur[i][0]+rj >= xZrut+r >= sur[i][0] and sur[i][1]+rj >= yZrut+r >= sur[i][1]:
    # wdcanvas.delete(str(i+1))
    # print(sur[i][0])
    # print(xZrut)
    # for i in range(len(sur)):
    # canvas.delete(sur[i])

    # canvas.delete(str(i))
    canvas.after(20, pohyb)


def zmena_smeru(event):
    global xPosun, yPosun
    if event.keysym == 'w':
        yPosun = -1
        xPosun = 0
    if event.keysym == 'a':
        xPosun = -1
        yPosun = 0
    if event.keysym == 's':
        yPosun = 1
        xPosun = 0
    if event.keysym == 'd':
        xPosun = 1
        yPosun = 0


xZrut = yZrut = 0
xPosun = 1
yPosun = 0
r = 50
rj = 20
N = 20
sur = []
canvas.create_oval(xZrut, yZrut, xZrut+r, yZrut+r, fill='blue', tags='zrut')

for i in range(N):
    x = random.randint(0, w-rj)
    if x >= r:
        y = random.randint(0, h-rj)
    else:
        y = random.randint(r, h-rj)
    canvas.create_oval(x, y, x+rj, y+rj, fill='red',tags=str(i))  # ,tags=str(i+1))
    sur.append([x, y])

pohyb()
canvas.bind_all('<Key>', zmena_smeru)
canvas.mainloop()
