from turtle import Turtle, Screen

blue_tutle = Turtle()
blue_tutle.color("blue")
space = 10
for x in range(15):
    blue_tutle.forward(space)
    blue_tutle.penup()
    blue_tutle.forward(space)
    blue_tutle.down()



screen = Screen()
screen.exitonclick()