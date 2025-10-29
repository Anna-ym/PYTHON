import turtle


screen = turtle.Screen()
screen.bgcolor("black")


pen = turtle.Turtle()
pen.color("magenta")
pen.speed(0)


for i in range(36):
    pen.circle(100)
    pen.right(10)


pen.hideturtle()
turtle.done()
