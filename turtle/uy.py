import turtle

screen = turtle.Screen()
screen.title("Turtle House")
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(3)


def draw_rectangle(color, width, height):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


t.penup()
t.goto(-100, -150)  # Move to starting position
t.pendown()
draw_rectangle("lightcoral", 200, 150)

t.hideturtle()
screen.mainloop()
