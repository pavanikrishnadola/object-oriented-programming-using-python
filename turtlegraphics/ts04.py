#color filling in shape using begin fill and end fill
#shape
from turtle import *
title("Turtle Graphics Example")
bgcolor("lightblue")
speed(1)
setup(600,400)
shape("turtle")
color("blue")
pencolor("brown")
width(3)
begin_fill()
fillcolor("yellow")
for i in range(4):
    forward(100)
    left(90)
end_fill()
done()