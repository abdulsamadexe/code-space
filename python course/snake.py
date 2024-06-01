import turtle as t
class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snake()
    def new_snake(self):
        turtle=t.Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()  
        turtle.goto(self.turtles[-1].xcor(),self.turtles[-1].ycor())
        self.turtles.append(turtle)
    def create_snake(self):
        x=-40
        y=0
        for _ in range(3):
            turtle=t.Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x,y)
            self.turtles.append(turtle)
            x+=20
    def move(self):
        for turtle in range(len(self.turtles)-1,0,-1):
            x=self.turtles[turtle-1].xcor()
            y=self.turtles[turtle-1].ycor()
            self.turtles[turtle].goto(x,y)
        self.turtles[0].forward(20)
    
    def up(self):
        if self.turtles[0].heading() !=270:
            self.turtles[0].setheading(90)


    def down(self):
        if self.turtles[0].heading()!=90:
            self.turtles[0].setheading(270)


    def left(self):
        if self.turtles[0].heading()!=0:
            self.turtles[0].setheading(180)


    def right(self):
        if self.turtles[0].heading()!=180:
            self.turtles[0].setheading(0)


