import turtle,random
screen=turtle.Screen()
screen.setup(width=500,height=400)
colors=["red", "green", "blue", "orange", "yellow",]
turtles=[]
x=-230
y=100
screen.bgcolor("black")

for _ in range(0,5):
    new_turtle=turtle.Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[_])
    new_turtle.goto(x,y)
    y-=30
    turtles.append(new_turtle)

user_guess=screen.textinput(title="Make your guess",prompt="Choose any color")


game_on=True
while game_on:
    for turtle in turtles:
        if turtle.xcor() >=230 and user_guess==turtle.pencolor():
            game_on=False
            print("You won the bet.",turtle.pencolor(),"won the game")
            break
        elif turtle.xcor() >=230 and user_guess!=turtle.pencolor():
            game_on=False
            print("You lost the bet.",turtle.pencolor()," was the winner ")
            break
        speed=random.randint(0,10)
        turtle.forward(speed)
# def move_forward():
#     tim.forward(20)
# def move_backward():
#     tim.right(180)
#     tim.forward(20)
# def move_left():
#     tim.left(20)
#     tim.forward(20)
# def move_right():
#     tim.right(20)
#     tim.forward(20))
# def clearscreen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key="s",fun=move_backward)
# screen.onkey(key="a",fun=move_left)
# screen.onkey(key="d",fun=move_right)
# screen.onkey(key="c",fun=clearscreen)

screen.exitonclick()


