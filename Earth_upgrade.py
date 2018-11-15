# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:59:26 2018

@author: Husarov_Max
"""
#Earth R = 149 p = 1 year
#Venus R = 107 p = 0.61 year
#Mars R = 206 p = 1.9 year
#Jupiter R = 778 p = 11.86 years
#Saturn R = 1513 p = 29.46 years
#Uran R = 2870 p = 84.5 years


import tkinter as tki
from math import pi, sin, cos


root = tki.Tk()
root.geometry('640x620+50+50')

canvas = tki.Canvas(root, width=1400, height=1000, bg='lightblue')
canvas.pack(padx=1, pady=1)

def get_oval(r, c, R):
    return canvas.create_oval(300-r+R, 300-r, 300+r+R, 300+r, fill=c)

sun = get_oval(20, 'yellow', 0)

R_earth = 200
r_earth = 15
alpha_earth = 0
earth = get_oval(r_earth, 'blue', R_earth)
orbita_earth = canvas.create_oval(300-R_earth, 300-R_earth,
                                 300+R_earth, 300+R_earth, dash=(2,2))

R_venus = int(200 * 107 / 149)
r_venus = 10
alpha_venus = 0
venus = get_oval(r_venus, 'pink', R_venus)
orbita_venus = canvas.create_oval(300-R_venus, 300-R_venus,
                                 300+R_venus, 300+R_venus, dash=(2,2))

R_mars = int(200 * 206 / 149)
r_mars = 10
alpha_mars = 0
mars = get_oval(r_mars, 'red', R_mars)
orbita_mars = canvas.create_oval(300-R_mars, 300-R_mars,
                                300+R_mars, 300+R_mars, dash=(2,2))

R_jupiter = int(200 * 278 / 149)
r_jupiter =  50
alpha_jupiter = 0
jupiter = get_oval(r_jupiter, 'brown', R_jupiter)
orbita_jupiter = canvas.create_oval(300-R_jupiter, 300-R_jupiter,
                                    300+R_jupiter, 300+R_jupiter, dash=(2,2))

R_saturn = int(200 * 378 / 149)
r_saturn = 30
alpha_saturn = 0
saturn = get_oval(r_saturn, 'violet', R_saturn)
orbita_saturn = canvas.create_oval(300-R_saturn, 300-R_saturn,
                                   300+R_saturn, 300+R_saturn, dash=(2,2))

R_uran = int(200 * 440 / 149)
r_uran = 25
alpha_uran = 0
uran = get_oval(r_uran, 'grey', R_uran)
orbita_uran = canvas.create_oval(300-R_uran, 300-R_uran,
                                   300+R_uran, 300+R_uran, dash=(2,2))


connection1 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='white')
connection2 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='white')
connection3 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='white')
connection4 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='white')
connection5 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='white')
connection6 = canvas.create_line(0, 0, 0, 0, dash=(1,1), fill='white')


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
    
    global alpha_jupiter
    alpha_jupiter += (5/11.86)
    if alpha_jupiter > 360: alpha_jupiter -= 360
    move_planet(jupiter, r_jupiter, R_jupiter, alpha_jupiter)
    
    global alpha_saturn
    alpha_saturn += (5/29.46)
    if alpha_saturn > 360: alpha_saturn -= 360
    move_planet(saturn, r_saturn, R_saturn, alpha_saturn)
    
    global alpha_uran
    alpha_uran += (5/84.5)
    if alpha_uran > 360: alpha_uran -= 360
    move_planet(uran, r_uran, R_uran, alpha_uran)
    
    connect(connection1, R_earth, alpha_earth, R_mars, alpha_mars)
    connect(connection2, R_venus, alpha_venus, R_mars, alpha_mars)
    connect(connection3, R_earth, alpha_earth, R_venus, alpha_venus)
    connect(connection4, R_jupiter, alpha_jupiter, R_uran, alpha_uran)
    connect(connection5, R_saturn, alpha_saturn, R_uran, alpha_uran)
    connect(connection6, R_jupiter, alpha_jupiter, R_saturn, alpha_saturn)
    
    
    root.after(100, roll)
    
root.after(0, roll)

root.mainloop()