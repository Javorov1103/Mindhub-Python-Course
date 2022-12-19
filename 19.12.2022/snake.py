import random
import turtle as t

t.bgcolor('yellow')

snake = t.Turtle()
snake.shape('square')
snake.color('red')
snake.speed(0)
snake.penup()
snake.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed(0)
leaf.hideturtle()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press space to START', align='center', font=("Arial",16, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    pass

def game_over():
    pass

def display_score(current_score):
    pass
def place_leaf():
    pass
def start_game():
    global game_started
    if game_started:
        return
    game_started = 0
    score = 0
    text_turtle.clear()
    
    snake_speed=2
    snake_lenght = 3
    snake.shapesize(1, snake_lenght,1)
    snake.showturtle()
    display_score(score)
    place_leaf()
    
    while True:
        snake.forward(snake_speed)
        if snake.distance(leaf) < 20:
            place_leaf()
            snake_lenght = snake_lenght + 1
            snake.shapesize(1,snake_lenght,1)
            snake_speed = snake_speed + 1
            score = score  + 10
            display_score(score)
        if outside_window(): 
            game_over()
            break
    
def move_up():
    pass
def move_down():
    pass
def move_left():
    pass
def move_right():
    pass

t.onkey(start_game,'space')
t.listen()
t.mainloop()

# t.done()