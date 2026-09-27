import colorgram
import turtle as t
import random

# used to extract color list from colorgram
# hirst_colors = colorgram.extract('OIP.webp', 10)
#
# colors = []
#
# for color in hirst_colors:
#     rgb = color.rgb  # e.g. (255, 151, 210)
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     color_tuple = (red, green, blue)
#     colors.append(color_tuple)
#
# print(colors)
t.colormode(255)
screen = t.Screen()
tim = t.Turtle()
tim.shape("turtle")

color_list =[(207, 153, 101), (22, 46, 138), (234, 226, 109), (222, 123, 166), (172, 51, 82), (55, 76, 156), (214, 58, 107), (155, 86, 52), (243, 222, 164), (59, 18, 33)]

tim.penup()
tim.setpos(-250,-200)

def paint_dots():
    for _ in range(0, 11):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)
        tim.pendown()

def new_line1():
    tim.penup()
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(50)
def new_line2():
    tim.penup()
    tim.right(90)
    tim.fd(50)
    tim.right(90)
    tim.fd(50)

for _ in range(0, 5):
    paint_dots()
    new_line1()
    paint_dots()
    new_line2()

tim.hideturtle()
screen.exitonclick()