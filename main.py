from hashlib import shake_128
from tkinter import *
import tkinter

root = Tk()
counter = 0 # переменная, в которой хранится номер клика мыши
coords = [] # координаты точек

def sign(x):
    if x >= 0: return 1
    return -1
def draw_dot(x,y,col='black'): # в tkinter нет возможности отрисовать точку, а потому рисуем очень маленький круг
    x1,y1 = x-1,y-1
    x2,y2 = x+1,y+1
    canvas.create_oval(x1, y1, x2, y2,fill=col,width=1,outline=col)
def simple(x1,y1,x2,y2): # первый простой алгоритм
    if x1 != x2:
        
        m = (y2-y1)/(x2-x1) # может выходить за пределы [-1;1] 
        
        if x1 > x2: 
            x1,x2 = x2,x1
            y1,y2 = y2,y1
        y = y1
        for x in range(x1,x2):
            draw_dot(x,round(y))
            y = y + m
       
    else:
        if y1 == y2:
            draw_dot(x,y)
        else: print('Error: vertical')
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
def BresenhamV4(x1,y1,x2,y2): # четырёхсвязная развёртка (третий алгоритм)
    x,y,dx,dy,s1,s2 = x1,y1,abs(x2-x1),abs(y2-y1),sign(x2-x1),sign(y2-y1)
    l = None
    if dy<dx: l = False
    else:
        l = True
        dx,dy = dy,dx
    e = 2*dy-dx
    for i in range(1,dx+dy):
        draw_dot(x,y)
        if e < 0:
            if l: y = y + s2
            else: x = x + s1
            e = e+2*dy
        else:
            if l : x = x + s1
            else: y = y + s2
            e = e - 2*dx
    draw_dot(x,y)
    pass



def Circle(x1,y1,x2,y2): # Чётвёртная функция (окружность)
    R = round(((x2-x1)**2 + (y2-y1)**2)**0.5)
    for x in range(0,R+1):
        y = y1 +  round((R**2 - x**2)**0.5)
        draw_dot(x + x1,y)
    for x in range(0,R+1):
        y = y1 -  round((R**2 - x**2)**0.5)
        draw_dot(x1-x,y)
    for x in range(0,R+1):
        y = y1 +  round((R**2 - x**2)**0.5)
        draw_dot(x1-x,y)
    for x in range(0,R+1):
        y = y1 -  round((R**2 - x**2)**0.5)
        draw_dot(x1+x,y)
        
    pass


# ДОООДЕЛАТЬ!!!!!!!!!!!!1
def BresenhamСircle(x1,y1,x2,y2): # Пятая функция (окружность) (работает криво)
    rad = ((x2-x1)**2 + (y2-y1)**2)**0.5 # радиус окружности
    x,y = 0,round(rad)
    e = 3-2*y
   
    while x < y:

        draw_dot(x1+x,y1+y)
        draw_dot(x1+y,y1+x)
        draw_dot(x1+y,y1-x)
        draw_dot(x1+x,y1-y)
        draw_dot(x1-x,y1-y)
        draw_dot(x1-y,y1-x)
        draw_dot(x1-y,y1+x)
        draw_dot(x1-x,y1+y)
        if e < 0:e = e+4*x+6
        else: 
            e = e+4*(x-y)+ 10
            y = y - 1
        x = x + 1 
    if x == y:
        draw_dot(x,y)
        draw_dot(y,x)
        draw_dot(y,-x)
        draw_dot(x,-y)
        draw_dot(-x,-y)
        draw_dot(-y,-x)
        draw_dot(-y,x)
        draw_dot(-x,y)
    pass



def callback(event): # метод отслеживания нажатий
    global counter,coords,var
    coords.append([int(event.x),int(event.y)])
    if counter >= 1: 
        print('Current click: ',counter + 1)
        print(coords)
     
      #  canvas.create_line(coords[0][0],coords[0][1],coords[1][0],coords[1][1]) # сделать тут свой метод отрисовки
        mode[var.get()](coords[0][0],coords[0][1],coords[1][0],coords[1][1]) # P.S сделать так чтобы пользователь мог выбирать режим посредством тыкания кнопок
        coords = []
        counter = 0
        
    else: 
        print('Current click: ',counter + 1)
        counter += 1
    
def clear(): # очистить холст
    canvas.delete("all") 

canvas= Canvas(root, width=800, height=600,bg='white')
mode = {'simple':simple,'BresenhamV8': BresenhamV8,'BresenhamV4': BresenhamV4,'Circle' : Circle,'BresenhamСircle': BresenhamСircle} # массив функциий (алгоритмов по которым будет делаться отрисовка)
# радиокнопки
var = StringVar()
var.set('BresenhamСircle')
for key in mode:
    rbtn = Radiobutton(text=key,variable=var,value=key)
    rbtn.pack()
# очистка холста
clsBtn = tkinter.Button(root,text='Очистить холст',command=clear)
clsBtn.pack()

canvas.bind("<Button-1>", callback)
canvas.pack()
root.mainloop()