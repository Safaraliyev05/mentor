import turtle

# Setup screen and turtle
screen = turtle.Screen()
screen.title("Turtle House")
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(3)


# Function to draw a rectangle
def draw_rectangle(color, width, height):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


# Function to draw a triangle
def draw_triangle(color, size):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


# Draw the house base
t.penup()
t.goto(-100, -150)  # Move to starting position
t.pendown()
draw_rectangle("lightcoral", 200, 150)

# Draw the roof
t.penup()
t.goto(-100, 0)  # Move to the top of the house
t.pendown()
draw_triangle("brown", 200)

# Draw a door
t.penup()
t.goto(-40, -150)  # Move to door position
t.pendown()
draw_rectangle("saddlebrown", 50, 90)

# Draw windows
# Left window
t.penup()
t.goto(-80, -50)  # Move to left window position
t.pendown()
draw_rectangle("lightblue", 40, 40)

# Right window
t.penup()
t.goto(40, -50)  # Move to right window position
t.pendown()
draw_rectangle("lightblue", 40, 40)

# Finish
t.hideturtle()
screen.mainloop()
