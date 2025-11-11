#pencolor,for loop for shape animation
#shape
from turtle import *
title("Turtle Graphics Example")
bgcolor("lightblue")
setup(600,400)
shape("turtle")
color("darkgreen")
pencolor("brown")
width(3)
for i in range(4):
    forward(100)
    left(90)
done()