
import turtle           # imports the turtle module

s = turtle.Screen()                  # generates the screen
my_turtle = turtle.Turtle()         # assigning different name to our turtle module

# generates the background color
turtle.bgcolor("orange")
turtle.pensize(6)
turtle.pencolor("red")

# for drawing circle
# my_turtle.circle(100)  
for i in range(3):
    def square():
        my_turtle.forward(90)
        my_turtle.right(90)

    square()

for i in range(5):
    def rectangle():
        my_turtle.forward(120)
        my_turtle.right(90)
        my_turtle.fillcolor("yellow")
    rectangle()

s.exitonclick()     # exits on click






