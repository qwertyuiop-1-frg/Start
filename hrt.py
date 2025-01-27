from turtle import *

def draw_heart():
    penup()
    goto(0,-200)
    pendown()
    begin_fill()
    color("red","red")
    left(140)
    forward(360)
    circle(-180,200)
    setheading(60)
    circle(-180,200)
    forward(360)
    end_fill()
    exitonclick()

draw_heart()
turtle.done()