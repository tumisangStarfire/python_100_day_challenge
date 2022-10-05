import colorgram
import random
from turtle import Turtle, Screen


screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 6)

rgb_extracted_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_extracted_colors.append(new_color)


def draw_hirst_painting():
    x_start_pos = -250
    y_start_pos = -250
    turtle = Turtle()
    #turtle.up()
    turtle.goto(x_start_pos, y_start_pos)
    steps = 25
    for x in range(10):
        for color in rgb_extracted_colors:
            turtle.dot(10,color)
            turtle.forward(steps)
            if turtle.xcor() == 300 or turtle.xcor() == -300:
                turtle.setheading(90)
                turtle.forward(10)
                turtle.left(90)
                turtle.setheading(90)
                turtle.right(90)




draw_hirst_painting()

screen.exitonclick()