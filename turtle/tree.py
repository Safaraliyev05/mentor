import turtle

screen = turtle.Screen()
screen.title("Turtle House")
screen.bgcolor("skyblue")
screen.screensize(800, 600)
t = turtle.Turtle()
t.speed(3)


def rectangle(color, width, height):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def triangle(color, size):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


t.penup()
t.goto(-200, -150)
t.pendown()
rectangle("brown", 50, 150)

t.penup()
t.goto(-250, 0)
t.pendown()
triangle('green', 150)

t.penup()
t.goto(-250, 130)
t.pendown()
triangle('green', 150)

t.penup()
t.goto(-250, 260)
t.pendown()
triangle('green', 150)

t.hideturtle()
screen.mainloop()
