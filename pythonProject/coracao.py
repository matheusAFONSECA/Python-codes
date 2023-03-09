import turtle
import time


pen = turtle.Turtle()


def curva():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def coracao():
    pen.fillcolor('black')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curva()
    pen.left(120)
    curva()
    pen.forward(112)
    pen.end_fill()


coracao()
pen.ht()
time.sleep(200)
