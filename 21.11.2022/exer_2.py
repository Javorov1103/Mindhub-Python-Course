import turtle as t
# Задача за рисуване на робот
# Дефинираме функцията за рисуване на правоъгълник
def draw_rectangle(a,b, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for i in range(1,3):
        t.forward(a)
        t.right(90)
        t.forward(b)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed("slow")
t.bgcolor("Dodger blue")

#feet
def draw_feet():
    t.goto(-100,-150)
    draw_rectangle(50,20,"blue")
    t.goto(-30, -150)
    draw_rectangle(50,20,"blue")

#legs
def draw_legs():
    t.goto(-25,-50)
    draw_rectangle(15,100,"grey")
    t.goto(-55,-50)
    draw_rectangle(-15,100,"grey")

#body
def draw_body():
    t.goto(-90,100)
    draw_rectangle(100,150,'red')

#right arm
def draw_right_arm():
    t.goto(-150,70)
    draw_rectangle(60,15,'grey')
    t.goto(-150,110)
    draw_rectangle(15,40,'grey')

#left arm
def draw_left_arm():
    t.goto(10,70)
    draw_rectangle(60,15,'grey')
    t.goto(55,110)
    draw_rectangle(15,40,'grey')

#neck
def draw_neck():
    t.goto(-50,120)
    draw_rectangle(15,20,'grey')
#head
def draw_head():
    t.goto(-85,170)
    draw_rectangle(80,50,'red')

#eyes
def draw_eyes():
    t.goto(-60,160)
    draw_rectangle(30,20,"white")
    t.goto(-55,155)
    draw_rectangle(5,5,'black')
    t.goto(-40,155)
    draw_rectangle(5,5,'black')

#mouth
def draw_mouth():
    t.goto(-65,135)
    draw_rectangle(40,5,'black')

def draw_robot():
    draw_feet()
    draw_legs()
    draw_body()
    draw_left_arm()
    draw_right_arm()
    draw_neck()
    draw_head()
    draw_eyes()
    draw_mouth()


draw_robot()

t.done()