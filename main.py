from tkinter import *
import tkinter

root = Tk()
counter = 0 # переменная, в которой хранится номер клика мыши
coords = [] # координаты точек
mode = [] # массив функциий (алгоритмов по которым будет делаться отрисовка)
def sign(x):
    if x >= 0: return 1
    return -1
def draw_dot(x,y,col='black'): # в tkinter нет возможности отрисовать точку, а потому рисуем очень маленький круг
    x1,y1 = x-1,y-1
    x2,y2 = x+1,y+1
    canvas.create_oval(x1, y1, x2, y2,fill=col,width=1,outline=col)
def simple(x1,y1,x2,y2): # первый простой алгоритм
    if x1 != x2: 
          
            m = (y2-y1)/(x2-x1)
            y = y1
            xs = min(x1,x2)
            xe = max(x1,x2)
            for x in range(xs,xe):
                draw_dot(x,round(y))
                y = y + m
                
    elif y1 == y2:
        draw_dot(x1,y1)
    elif y1 != y2:
        print('Error : vertical!')
    pass
def BresenhamV8(x1,y1,x2,y2): # восьмикратная развертка (второй алгоритм)
    l = None 
    x,y,dx,dy = x1,y1,abs(x2-x1),abs(y2-y1)
    s1,s2 = sign(x2-x1),sign(y2-y1)
    if dy > dx:
        dx,dy = dy,dx
        l = True
    else: l = False
    e = 2*dy-dx
    for i in range(1,dx+1):
        draw_dot(x,y)
        while e >= 0:
            if l:
                x = x + s1
            else:
                y = y + s2
            e = e - 2*dx
        if l:
            y = y + s2
        else: 
            x = x + s1
        e = e + 2*dy
    draw_dot(x,y)



    pass
def callback(event): # метод отслеживания нажатий
    global counter,coords
    coords.append([int(event.x),int(event.y)])
    if counter >= 1: 
        print(coords)
      #  canvas.create_line(coords[0][0],coords[0][1],coords[1][0],coords[1][1]) # сделать тут свой метод отрисовки
        BresenhamV8(coords[0][0],coords[0][1],coords[1][0],coords[1][1])
        coords = []
        counter = 0
        
    else: 
        print('Current click: ',counter + 1)
        counter += 1
    
def clear(): # очистить холст
    canvas.delete("all") 

canvas= Canvas(root, width=800, height=600)
clsBtn = tkinter.Button(root,text='Очистить холст',command=clear)

clsBtn.pack()
clsBtn.place(x=400,y=560)
canvas.bind("<Button-1>", callback)
canvas.pack()
root.mainloop()