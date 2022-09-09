from tkinter import *

root = Tk()
counter = 0 # переменная, в которой хранится номер клика мыши
coords = [] # координаты точек
mode = [] # режим,в котором происходит рисование
def draw_dot(x,y): # в tkinter нет возможности отрисовать точку, а потому рисуем очень маленький круг
    x1,y1 = x-1,y-1
    x2,y2 = x+1,y+1
    canvas.create_oval(x1, y1, x2, y2,fill='black',width=0)
def callback(event):
    global counter,coords
    coords.append([int(event.x),int(event.y)])
    if counter >= 1: 
        print(coords)
        canvas.create_line(coords[0][0],coords[0][1],coords[1][0],coords[1][1]) # сделать тут свой метод отрисовки
        coords = []
        counter = 0
        draw_dot(120,10)
    else: 
        print('Current click: ',counter + 1)
        counter += 1
    
    

canvas= Canvas(root, width=800, height=600)

canvas.bind("<Button-1>", callback)
canvas.pack()
root.mainloop()