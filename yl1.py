import turtle
from random import random, randrange

def koch_curve(turtle, steps, length):
    if steps == 0:
        turtle.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, steps - 1, length / 3)
            turtle.left(angle)

def koch_snowflake(turtle, steps, length):
    turtle.begin_poly()

    for _ in range(3):
        koch_curve(turtle, steps, length)
        turtle.right(120)

    turtle.end_poly()

    return turtle.get_poly()

turtle.speed("fastest")

turtle.register_shape("snowflake", koch_snowflake(turtle.getturtle(), 3, 100))

turtle.reset()

turtle.penup()

turtle.shape("snowflake")

width, height = turtle.window_width() / 2, turtle.window_height() / 2

for _ in range(24):
    turtle.color((random(), random(), random()), (random(), random(), random()))
    turtle.goto(randrange(-width, width), randrange(-height, height))
    turtle.stamp()

turtle.done()