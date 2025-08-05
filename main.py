from turtle import *

t = Turtle()
t.shape("turtle")
t.color("red")
t.speed(100 )
scr = t.getscreen()
scr.listen()

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw(x,y):
    t.goto(x, y)



def red():
    t.color("red")

def blue():
    t.color("blue")

def up():
    t.goto(t.xcor(), t.ycor() + 10)

def down():
    t.goto(t.xcor(), t.ycor() - 10)

def left():
    t.goto(t.xcor() - 10, t.ycor())

def right():
    t.goto(t.xcor() + 10, t.ycor())

t.ondrag(draw)
scr.onscreenclick(move)
scr.onkey(red, "r")
scr.onkey(blue, "b")
scr.onkey(up, "w")
scr.onkey(down, "s")
scr.onkey(left, "a")
scr.onkey(right, "d")


def fill():
    t.begin_fill()

def efill():
    t.end_fill()

scr.onkey(fill, 'f')
scr.onkey(efill, 'e')
done()