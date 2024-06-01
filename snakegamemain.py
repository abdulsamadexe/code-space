import turtle as t
import time
from snake import Snake
from food import Food
from snakescoreboard import Scoreboard
screen=t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("snakegame")
screen.tracer(0)

# snake body
snake=Snake()
food=Food()
scoreboard=Scoreboard()
#controlling the snake
screen.listen()

screen.onkey(key="w",fun=snake.up)

screen.onkey(key="s",fun=snake.down)

screen.onkey(key="a",fun=snake.left)

screen.onkey(key="d",fun=snake.right)


screen.update()

#snake movement
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtles[0].distance(food)<15:
        food.refresh()
        scoreboard.new_score()
        snake.new_snake()
    if snake.turtles[0].xcor()>290 or snake.turtles[0].xcor()<-290 or snake.turtles[0].ycor()>290 or snake.turtles[0].ycor()<-290:
        game_on=False
        scoreboard.gameover()
    for i in range(1,len(snake.turtles)-1):
        if snake.turtles[0].distance(snake.turtles[i])<10:
            game_on=False
            scoreboard.gameover()





    

    






screen.exitonclick()

