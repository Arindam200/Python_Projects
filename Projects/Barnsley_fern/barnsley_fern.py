'''
simulation of barnsley fern (fractal) using python3.
Author-Ashutosh(0Pixel0)
'''

import turtle
import random

pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()

x = 0
y = 0
for n in range(11000):
    pen.goto(65 * x, 37 * y - 252)  # scaling
    pen.pendown()
    pen.dot(3)
    pen.penup()
    r = random.random()
    if r < 0.01:
        x, y =  0.00 * x + 0.00 * y,  0.00 * x + 0.16 * y + 0.00
    elif r < 0.86:
        x, y =  0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60
    elif r < 0.93:
        x, y =  0.20 * x - 0.26 * y,  0.23 * x + 0.22 * y + 1.60
    else:
        x, y = -0.15 * x + 0.28 * y,  0.26 * x + 0.24 * y + 0.44