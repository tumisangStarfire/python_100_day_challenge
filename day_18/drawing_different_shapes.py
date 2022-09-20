import random
from turtle import  Turtle,Screen


steps = 100

colors = ["red", "orange", "yellow", "pink", "grey", "blue", "DeepSkyBlue", "SeaGreen"]

for x in range(3, 10):
    number_of_sides = x
    angle = round(360 / number_of_sides)
    turtle = Turtle()
    turtle.color(random.choice(colors))
    for _ in range(number_of_sides):
        turtle.forward(steps)
        turtle.right(angle)
        number_of_sides + 1










screen = Screen()
screen.exitonclick()