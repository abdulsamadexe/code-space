import turtle
import prettytable

# timmy=turtle.Turtle()

# timmy.color('red')
# print(timmy.shape('turtle'))
# timmy.forward(100)
# my_screen=turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
table = prettytable.PrettyTable()

table.add_column("Pokemon",["pikachu","squirtel",'charmander'])
table.add_column("Type",["electric",'fire','water'])
table.align="l"
print(table)