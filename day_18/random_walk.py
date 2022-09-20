import random
from turtle import Turtle,Screen


screen = Screen()
screen.colormode(255)

def generate_rgb_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

def random_walk():
    directions = [0, 90, 180, 270]
    colors = ["red", "orange", "yellow", "pink", "grey", "blue", "DeepSkyBlue", "SeaGreen"]
    turtle = Turtle()
    turtle.width(5)
    for x in range(200):
        turtle_color = generate_rgb_color()
        print(turtle_color)
        turtle.color(turtle_color[0], turtle_color[1], turtle_color[2])
        turtle.forward(30)
        turtle.setheading(random.choice(directions))


random_walk()


screen.exitonclick()