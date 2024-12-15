import turtle

# Setup screen and turtle
screen = turtle.Screen()
screen.title("Turtle Castle")
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.speed(6)


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


# Function to draw a square (used for battlements)
def draw_square(color, size):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


# Draw the main wall
def draw_wall():
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    draw_rectangle("gray", 300, 100)


# Draw a tower
def draw_tower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_rectangle("darkgray", 60, 150)

    # Draw battlements
    for i in range(3):
        t.penup()
        t.goto(x + i * 20, y + 150)
        t.pendown()
        draw_square("darkgray", 20)


# Draw the castle gate
def draw_gate():
    t.penup()
    t.goto(-40, -100)
    t.pendown()
    draw_rectangle("brown", 80, 70)


# Draw the entire castle
def draw_castle():
    # Draw towers
    draw_tower(-180, -100)  # Left tower
    draw_tower(120, -100)  # Right tower

    # Draw the main wall
    draw_wall()

    # Draw the gate
    draw_gate()


# Execute the drawing
draw_castle()

# Finish up
t.hideturtle()
screen.mainloop()
