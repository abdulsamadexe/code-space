import turtle
import random
import colorgram
colors=colorgram.extract("image.jpg",30)
turtle.colormode(255)
colors=[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), 
(232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle1=turtle.Turtle()
turtle1.shape("turtle")
for i in range(10):
    for a in range(10):
        turtle1.pencolor(random.choice(colors))
        turtle1.pendown()
        turtle1.dot(10)
        turtle1.penup()
        turtle1.forward(20)
    turtle1.left(90)
    turtle1.forward(10)
    turtle1.left(90)
    turtle1.forward(200)
    turtle1.right(90)
    turtle1.forward(10)
    turtle1.right(90)


directions=[90,180,270,360]
turtle1.speed("fastest")

# for x in range(10000):
#     r=random.randint(0,255)
#     b=random.randint(0,255)
#     g=random.randint(0,255)
#     color=(r,g,b)
#     turtle1.pencolor(color)
#     turtle1.forward(50)
#     turtle1.setheading(random.choice(directions))

# for a in range(int(360/10)):
#     r=random.randint(0,255)
#     b=random.randint(0,255)
#     g=random.randint(0,255)
#     color=(r,g,b)
#     turtle1.pencolor(color)
#     turtle1.circle(100)
#     turtle1.left(10)




screen=turtle.Screen()
screen.exitonclick()
