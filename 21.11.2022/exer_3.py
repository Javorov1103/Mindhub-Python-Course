import turtle as t
from itertools import cycle

t.bgcolor("black")
t.pensize(4)
t.speed("fast")
colors = cycle(['red','orange','yellow','green','blue','purple'])
# Създай функция за чертане на спирала
def draw_circle(radius, angle, shift):
    color = next(colors)
    t.pencolor(color)
    t.cricle(radius)
    t.right(angle)
    t.forward(shift)
    draw_circle(radius+5,angle+1,shift+1)


draw_circle(30, 0, 1)


