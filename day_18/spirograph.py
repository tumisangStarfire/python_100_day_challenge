import random
from turtle import Turtle, Screen


screen = Screen()
screen.colormode(255)

def generate_rgb_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

def draw_spirograph():
    turtle = Turtle()
    for x in range(200):

        turtle.color(generate_rgb_color())
        turtle.circle(50)
        turtle.setheading(turtle.heading()+10)

draw_spirograph()

screen.exitonclick()