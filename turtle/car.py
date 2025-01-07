import turtle


def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_ferrari():
    turtle.speed(3)

    draw_rectangle("red", -150, 0, 300, 50)
    draw_rectangle("red", -100, 50, 200, 40)

    draw_rectangle("black", -90, 55, 80, 30)
    draw_rectangle("black", 20, 55, 80, 30)

    draw_circle("black", -100, -20, 30)
    draw_circle("black", 100, -20, 30)
    draw_circle("gray", -100, -20, 15)
    draw_circle("gray", 100, -20, 15)

    turtle.penup()
    turtle.goto(-150, -10)
    turtle.pendown()



screen = turtle.Screen()
screen.title("Ferrari Side View")
screen.bgcolor("lightblue")

draw_ferrari()

turtle.hideturtle()
screen.mainloop()
