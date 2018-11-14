# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:59:26 2018

@author: Админ
"""
#Earth R = 149 p = 1 year
#Venus R = 107 p = 0.61 year
#Mars R = 206 p = 1.9 year

import tkinter as tki
from math import pi, sin, cos


root = tki.Tk()
root.geometry('640x620+50+50')

canvas = tki.Canvas(root, width=600, height=600, bg='lightblue')
canvas.pack(padx=10, pady=10)

def get_oval(r, c, R):
    return canvas.create_oval(300-r+R, 300-r, 300+r+R, 300+r, fill=c)

sun = get_oval(20, 'yellow', 0)

R_earth = 200
r_earth = 15
alpha_earth = 0
earth = get_oval(r_earth, 'blue', R_earth)
orbita_earth = canvas.create_oval(300-R_earth, 300-R_earth,
                                 300+R_earth, 300+R_earth, dash=(5,5))

R_venus = int(200 * 107 / 149)
r_venus = 10
alpha_venus = 0
venus = get_oval(r_venus, 'pink', R_venus)
orbita_venus = canvas.create_oval(300-R_venus, 300-R_venus,
                                 300+R_venus, 300+R_venus, dash=(5,5))

R_mars = int(200 * 206 / 149)
r_mars = 10
alpha_mars = 0
mars = get_oval(r_mars, 'red', R_mars)
orbita_mars = canvas.create_oval(300-R_mars, 300-R_mars,
                                300+R_mars, 300+R_mars, dash=(5,5))

connection1 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='green')
connection2 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='green')
connection3 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='green')

def get_coords(R, a):
    a = a / 180.0 * pi
    x = 300 + R * cos(a)
    y = 300 - R * sin(a)
    return(x, y)

def connect(connect, R1, a1, R2, a2):
    x1, y1 = get_coords(R1, a1)
    x2, y2 = get_coords(R2, a2)
    canvas.coords(connect, x1, y1, x2, y2)
    
def move_planet(planet, r, R, alpha):
    angle_rad = alpha / 180.0 * pi
    x = 300 + R * cos(angle_rad)
    y = 300 - R * sin(angle_rad)
    canvas.coords(planet, x - r, y - r, x + r, y + r)
    
def roll():
    global alpha_earth
    alpha_earth += 5
    if alpha_earth > 360: alpha_earth -= 360
    move_planet(earth, r_earth, R_earth, alpha_earth)
    #print(alpha_earth)
    
    global alpha_venus
    alpha_venus += (5/0.6)
    if alpha_venus > 360: alpha_venus -= 360
    move_planet(venus, r_venus, R_venus, alpha_venus)
    
    global alpha_mars
    alpha_mars += (5/1.9)
    if alpha_mars > 360: alpha_mars -= 360
    move_planet(mars, r_mars, R_mars, alpha_mars)
    
    connect(connection1, R_earth, alpha_earth, R_mars, alpha_mars)
    connect(connection2, R_venus, alpha_venus, R_mars, alpha_mars)
    connect(connection3, R_earth, alpha_earth, R_venus, alpha_venus)
    
    root.after(100, roll)
    
root.after(0, roll)

root.mainloop()