
def draw_audi(t, initial_x, radius):
    t.speed(10)
    t.penup()
    t.goto(initial_x,0)
    t.pendown()
    for i in range(4):
        t.circle(radius)
        t.penup()
        initial_x += initial_x + 50
        t.goto(initial_x,0)
        t.pendown()