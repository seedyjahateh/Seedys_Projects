######################################################################
# Author: Seedy M. Jahateh
# Username: jahatehs
#
# Assignment: A03:

######################################################################
# Repo link: https://github.com/Berea-College-CSC-226/a03-master-sp23.git
# Google Doc link: https://docs.google.com/document/d/1Bs1iYHj0WV5NxUfJw0a10Iw9logLJSeXv2-2HxR8beU/edit?usp=sharing
########################################################################################

import turtle
from turtle import *


def position_update(x, y):
    """Changes the turtle position."""
    penup()
    goto(x, y)
    pendown()


def letters():
    """Writes the letters (boy)."""
    position_update(-250, 0)
    color('#000000')
    style = ('Century Gothic', 150)
    write('b o y', font=style)


def glasses():
    """Draws the glasses."""
    position_update(-125, 100)
    fillcolor("#FFFFFF")
    begin_fill()
    setheading(30)
    a = 0.5

    for i in range(60):
        if 0 <= i < 30:
            a += 0.05
            right(1)
            forward(a)
        else:
            a -= 0.05
            right(1)
            forward(a)
    end_fill()
    position_update(55, 95)
    setheading(15)
    forward(160)


def eyes(x, y):
    """Draws the eyes."""
    position_update(x, y)
    fillcolor('#FFFFFF')

    begin_fill()

    setheading(60)
    a = 0.6
    for i in range(60):
        if 0 <= i < 30:
            a += 0.05
            right(2)
            forward(a)
        else:
            a -= 0.05
            right(2)
            forward(a)
    setheading(240)
    a = 0.6
    for i in range(60):
        if 0 <= i < 30:
            a += 0.05
            right(2)
            forward(a)
        else:
            a -= 0.05
            right(2)
            forward(a)

    position_update(x + 35, y)
    dot(30, 'black')
    end_fill()


def hair():
    """Draws the hair."""
    position_update(137, 150)
    setheading(115)
    forward(48)
    for i in range(4):
        setheading(195)
        forward(100)
        setheading(80)
        forward(30)

    def hair_part(angle):
        setheading(angle)
        a = 3
        for j in range(60):
            if 0 <= j < 30:
                a += 0.05
                right(1.5)
                forward(a)

            else:
                a -= 0.05
                right(1)
                forward(a)
        setheading(angle + 160)
        forward(30)

    hair_part(80)
    hair_part(40)
    hair_part(355)


def ear():
    """Draws the ear."""
    position_update(210, 130)
    setheading(40)
    a = 0.6
    for i in range(90):
        if 0 <= i < 30:
            a += 0.02
            right(1.5)
            forward(a)
        elif 30 <= i < 60:
            a += 0.15
            right(4)
            forward(a)
        elif 60 <= i < 70:
            forward(a - 0.8)
        else:
            a -= 0.05
            right(8)
            forward(a - 1)
    position_update(215, 90)
    setheading(30)
    a = 1
    for i in range(60):
        if 0 <= i < 30:
            right(4.5)
            forward(a)
        else:
            right(1)
            forward(a + 0.5)


def face():
    """Draws the face."""
    position_update(160, 10)
    setheading(245)
    d = 0.5
    for i in range(270):
        if 0 <= i < 40:
            left(d - 0.2)
            forward(3)

        elif 40 <= i < 70:
            right(d)
            forward(1.5)

        elif 70 <= i < 120:
            right(d)
            forward(1)

        elif 120 <= i < 160:
            right(d + 0.2)
            forward(2.1)

        elif 160 <= i < 200:
            right(d + 0.1)
            forward(2.5)

        elif 200 <= i < 240:
            right(d + 0.5)
            forward(2)

        elif 240 <= i < 270:
            right(d + 0.5)
            forward(6)
    forward(50)


def nose():
    """Draws the nose."""
    position_update(-90, 60)
    setheading(270)
    forward(10)
    d = 1
    for i in range(100):
        if 0 <= i < 20:
            right(d + 0.5)
            forward(2.5)

        elif 30 <= i < 40:
            right(d + 0.5)
            forward(1)

        elif 40 <= i < 60:
            left(d + 3.5)
            forward(1.5)

        elif 60 <= i < 80:
            left(d + 3.5)
            forward(1)

        elif 80 <= i < 100:
            right(d + 2)
            forward(1)


def mouth():
    """Draws the mouth."""
    position_update(-140, -70)
    setheading(330)
    a = 2
    for i in range(60):
        if 0 <= i < 30:
            left(1)
            forward(a)


        else:
            left(1)
            forward(a)
    setheading(250)
    a = 2.5
    for i in range(60):
        if 0 <= i < 30:
            right(2)
            forward(a)
        else:
            right(2.6)
            forward(a)
    forward(10)
    position_update(-120, -140)
    setheading(330)
    a = 1
    for i in range(60):
        if 0 <= i < 30:
            left(1)
            forward(a)
        else:
            left(1)
            forward(a)


def neck():
    """Draws the neck."""
    position_update(-120, -202)
    setheading(270)
    a = 1.5
    for i in range(60):
        if 0 <= i < 30:
            right(0.5)
            forward(a)
        else:
            right(0.5)
            forward(a)
    position_update(90, -178)
    setheading(270)
    a = 2.5
    for i in range(60):
        if 0 <= i < 30:
            left(1)
            forward(a)
        else:
            left(1)
            forward(a)


def boy():
    """This is the main function that calls all the other functions"""
    letters()
    glasses()
    eyes(-215, 100)
    eyes(-30, 100)
    hair()
    ear()
    face()
    nose()
    mouth()
    neck()


# screen = turtle.Screen()
# turtle.screensize(400, 400, '#00FFFF')
if __name__ == '__main__':
    screen = turtle.Screen()
    screen.screensize(400, 400, '#00FFFF')
    screen.setup(width=1.0, height=1.0)
    boy()
    mainloop()
